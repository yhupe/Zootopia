import json


def load_data(file_path):
    """ Loads a JSON file """

    with open(file_path, "r") as fileobj:
        data = json.load(fileobj)
        return data

animals_data = load_data("animals_data.json")


def animal_wanted_poster(data):
    """Prints Name, Diet, Location, Type of each animal in the .json file"""

    for animal in data:
        print(f"Name: {animal['name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        print(f"Locations: {animal['locations'][0]}")

        if not animal['characteristics'].get('type', 'not existing') == 'not existing':
            print(f"Type: {animal['characteristics']['type']}")
        else:
            pass

        print()


animal_wanted_poster(animals_data)
