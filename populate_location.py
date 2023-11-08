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
    fields = "school.name,school.zip,school.city,school.state,latest.school.region_id,school.locale"

    api_request = f"{base_url}fields={fields}&api_key={config.API_KEY}&page={page_num}&_per_page=100"

    re = requests.get(api_request)
    data = re.json()

    return data


def clean_loc_data(data: dict) -> dict:
    clean_data = {}
    for school in data["results"]:
        clean_data["name"] = school["school.name"]
        print(school)
        break

    return clean_data


def populate_db() -> None:
    """
    psuedocode:
    1. make call
    2. get data
    3. clean data
    4. insert into db
    """
    page_num = 0

    data = get_loc_data(page_num)
    clean_loc_data(data)
    return


populate_db()

connection.commit()
