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


def get_loc_data(page_num: int) -> dict:
    base_url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?"
    fields = "school.name,latest.school.operating,school.zip,school.city,school.state,latest.school.region_id,school.locale"

    api_request = f"{base_url}fields={fields}&api_key={config.API_KEY}&page={page_num}&_per_page=100"

    re = requests.get(api_request)
    data = re.json()

    return data


def populate_db() -> None:
    page_num = 0
    make_call = True

    while make_call:
        data = get_loc_data(page_num)

        # Check if the API response contains results.
        if data["results"] != []:
            # Iterate through the schools in the API response.
            for school in data["results"]:
                try:
                    if school["latest.school.operating"] == 1:
                        print(f"Processing school {school['school.name']}")

                        school_id = location_dict[school["school.name"]]
                        cursor.execute(
                            "INSERT INTO location (school_id, zipcode, city, state, region, locale) VALUES (?, ?, ?, ?, ?, ?)",
                            (
                                school_id,
                                school["school.zip"],
                                school["school.city"],
                                school["school.state"],
                                school["latest.school.region_id"],
                                school["school.locale"],
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
