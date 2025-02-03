import requests
import json

animal_url = "https://api.api-ninjas.com/v1/animals"
my_api_key = "+kAwtvHVtZmB9W0KfmYwTg==IVHZoWi6avk8SiLk"


def load_data(file_path):
    """Receives 'animals_data.json',
    Loads a JSON file """

    with open(file_path, "r") as fileobj:
        data = json.load(fileobj)
        return data


def get_animal_data_by_name(url, api_key, animal):
    """Sends a GET request to the animals API in order to fetch
     animals data according to the animal the user is looking for by
     entering a name"""

    search_query = f"?name={animal}"
    response = requests.get(url + search_query, headers={'X-Api-Key': api_key})
    response_json = response.json()

    return response_json


def animal_card(data, animal):
    """Receives 'get_animals_data_by_name',
    Prints Name, Diet, Location, Type of each animal in the .json file"""

    if data:

        output = ""

        for animal in data:
            output += '<li class="cards__item">'
            output += f'<div class="card__title">{animal['name']}</div>'
            output += '<div class="card__text">'
            output += '<ul>'
            output += f"<li><strong>Diet:</strong> {animal['characteristics']
            ['diet']}</li>"
            output += f"<li><strong>Locations:</strong> {animal['locations']
            [0]}</li>"

            if not (animal['characteristics'].get('type', 'not existing')
                    == 'not existing'):
                output += f"<li><strong>Type:</strong> {animal['characteristics']
                ['type']}</li>"
            else:
                pass
            output += '</ul>'
            output += '</div>'
            output += '</li>'

    else:
        output = f'<div class="card__title">Unfortunately, your search for "{animal}" did not show any results!</div>'

    return output


def read_html_template(file_path):
    """Receives 'animals_template.html'
    Reads the html page which is supposed to display the animal information"""

    with open(file_path, "r") as fileobj:
        page_content = fileobj.readlines()

        html_page_content_string = ""

        for line in page_content:
            html_page_content_string += f"{line}\n"

    return html_page_content_string


def write_animals_with_data(html_template, animal_cards):

    filled_html = html_template.replace("__REPLACE_ANIMALS_INFO__",
                                        animal_cards)

    with open("animals.html", "w") as fileobj:
        fileobj.write(filled_html)


def main():

    #animals_data = load_data("animals_data.json")
    animal_name = input("Please enter an animal name here: ").strip()
    animals_data_from_api = get_animal_data_by_name(animal_url, my_api_key, animal_name)
    animal_information = animal_card(animals_data_from_api, animal_name)
    html_template = read_html_template("animals_template.html")
    write_animals_with_data(html_template, animal_information)


if __name__ in "__main__":
    main()