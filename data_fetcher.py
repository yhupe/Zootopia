import requests
import os
from dotenv import load_dotenv

load_dotenv()

animal_url = "https://api.api-ninjas.com/v1/animals"
my_api_key = os.getenv('my_api_key')


def fetch_data(animal):
    """ Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary"""

    search_query = f"?name={animal}"
    response = requests.get(animal_url + search_query, headers={'X-Api-Key': my_api_key})
    response_json = response.json()

    return response_json


