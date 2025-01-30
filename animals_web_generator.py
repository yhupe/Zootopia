import json


def load_data(file_path):
    """Receives 'animals_data.json',
    Loads a JSON file """

    with open(file_path, "r") as fileobj:
        data = json.load(fileobj)
        return data


def animal_card(data):
    """Receives 'animals_data',
    Prints Name, Diet, Location, Type of each animal in the .json file"""

    output = ""

    for animal in data:
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        output += f"Locations: {animal['locations'][0]}<br/>\n"

        if not animal['characteristics'].get('type', 'not existing') == 'not existing':
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        else:
            pass

        output += '</li>'

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

    filled_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_cards)

    with open("animals.html", "w") as fileobj:
        fileobj.write(filled_html)


def main():

    animals_data = load_data("animals_data.json")
    animal_information = animal_card(animals_data)
    html_template = read_html_template("animals_template.html")
    write_animals_with_data(html_template, animal_information)



if __name__ in "__main__":
    main()