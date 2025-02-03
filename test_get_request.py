import json
import requests

animal_url = "https://api.api-ninjas.com/v1/animals"
my_api_key = "+kAwtvHVtZmB9W0KfmYwTg==IVHZoWi6avk8SiLk"

def get_animal_data_by_name(url, api_key):
    """Sends a GET request to the animals API in order to fetch
     animals data according to the animal the user is looking for by
     entering a name"""

    animal_name = input("Please enter an animal name here: ").strip()
    search_query = f"?name={animal_name}"
    response = requests.get(url + search_query, headers={'X-Api-Key': api_key})
    response_json = response.json()

    return response_json

animal_data = get_animal_data_by_name(animal_url, my_api_key)
print(animal_data)