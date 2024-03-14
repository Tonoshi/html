import requests

from entity.person import Person
from entity.planet import Planet
from entity.ship import Ship


class StarWarsApi:

    def __init__(self):
        self.base_url = 'https://swapi.dev'

    def get_entity(self, entity, entity_id):
        url = f'{self.base_url}/api/{entity}/{entity_id}/'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f'Неможливо отримати дані про сутності {entity} з ідентифікатором {entity_id}')

    def get_person(self, person_id):
        person_dict = self.get_entity('people', person_id)
        return Person(person_dict)

    def get_planet(self, planet_id):
        planet_dict = self.get_entity('planets', planet_id)
        return Planet(planet_dict)
    def get_ship(self, ship_id):
        ship_dict = self.get_entity('ships', ship_id)
        return Ship(ship_dict)
