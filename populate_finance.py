import sqlite3, config
import requests


connection = sqlite3.connect(config.DB_FILE)

connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute(
    """
    SELECT id, name FROM school
    """
)

rows = cursor.fetchall()

schools = []
location_dict = {}
for row in rows:
    school = row["name"]
    schools.append(school)
    location_dict[school] = row["id"]


def get_finance_data(page_num: int) -> dict:
    base_url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?"
    fields = "school.name,latest.school.operating,latest.cost.attendance.academic_year,latest.cost.tuition.in_state,latest.cost.tuition.out_of_state"

    api_request = f"{base_url}fields={fields}&api_key={config.API_KEY}&page={page_num}&_per_page=100"

    re = requests.get(api_request)
    data = re.json()

    return data


def populate_db() -> None:
    page_num = 0
    make_call = True

    while make_call:
        data = get_finance_data(page_num)

        # Check if the API response contains results.
        if data["results"] != []:
            # Iterate through the schools in the API response.
            for school in data["results"]:
                try:
                    if school["latest.school.operating"] == 1:
                        print(f"Processing school {school['school.name']}")

                        school_id = location_dict[school["school.name"]]
                        cursor.execute(
                            "INSERT INTO finance (school_id, cost4a, in_state_tuition, out_state_tuition) VALUES (?, ?, ?, ?)",
                            (
                                school_id,
                                school["latest.cost.attendance.academic_year"],
                                school["latest.cost.tuition.in_state"],
                                school["latest.cost.tuition.out_of_state"],
                            ),
                        )
                except Exception as e:
                    # Print the school name and any exceptions that occur during insertion.
                    print(school["school.name"])
                    print(e)

            # Increment the page number to retrieve the next page of data.
            page_num += 1

        else:
            # If the API response is empty, exit the loop.
            make_call = False
    return


populate_db()

connection.commit()
