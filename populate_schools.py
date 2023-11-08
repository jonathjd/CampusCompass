import sqlite3, config
import requests

connection = sqlite3.connect(config.DB_FILE)

cursor = connection.cursor()

# Initialize variables for pagination and API endpoint.
page_num = 0
base_url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?"
fields = "school.name,school.school_url,latest.school.operating"
make_call = True

# Start a loop to retrieve data from the API.
while make_call:
    api_request = f"{base_url}fields={fields}&api_key={config.API_KEY}&page={page_num}&_per_page=100"

    re = requests.get(api_request)
    data = re.json()

    # Check if the API response contains results.
    if data["results"] != []:
        # Iterate through the schools in the API response.
        for school in data["results"]:
            try:
                if school["latest.school.operating"] == 1:
                    cursor.execute(
                        "INSERT INTO school (name, url) VALUES (?, ?)",
                        (school["school.name"], school["school.school_url"]),
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

connection.commit()
