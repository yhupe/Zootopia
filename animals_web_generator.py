import data_fetcher



def animal_card(data, animal):
    """ Receives list of dictionary structure with fetched data for
    the animal a user is searching for + the name searched for.
    Returns Name, Diet, Location, Type of the respective animal in
    output variable already in html format, if there is no data for the
     search query,a notification message is returned as output"""

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
        output = f'<div class="card__title_not_found">Unfortunately, your search for "{animal}" did not show any results!</div>'

    return output


def read_html_template(file_path):
    """ Receives 'animals_template.html'
    Reads the html template which is supposed to display the
    animal information and returns a string with the content of
    the html text file"""

    with open(file_path, "r") as fileobj:
        page_content = fileobj.readlines()

        html_page_content_string = ""

        for line in page_content:
            html_page_content_string += f"{line}\n"

    return html_page_content_string


def write_animals_with_data(html_template, animal_cards):
    """ Receives the string from the html page template,
    replaces a certain part in the html body with the
    respective animal information string in html format
    and safes the generated html code in a file 'animals.html' """

    filled_html = html_template.replace("__REPLACE_ANIMALS_INFO__",
                                        animal_cards)

    with open("animals.html", "w") as fileobj:
        fileobj.write(filled_html)


def main():
    """ Asks the User for an animal to enter,
    then calls the data fetcher to fetch all data based on the input
    and calls following functions to read the html template and to generate
    html code with real animal information"""

    animal_name = input("Please enter an animal name here: ").strip()
    animals_data_from_api = data_fetcher.fetch_data(animal_name)
    animal_information = animal_card(animals_data_from_api, animal_name)
    html_template = read_html_template("animals_template.html")
    write_animals_with_data(html_template, animal_information)


if __name__ in "__main__":
    main()