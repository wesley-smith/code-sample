from unittest import TestCase

from city import City
from power import PowerPlant


class CityTest(TestCase):
    def test_constructor(self):
        name = "Fooville"
        population = 10_000
        demand = 100_000_000
        plants = (PowerPlant(10_000, "fossil"),)
        city = City(name, population, demand, plants)
        self.assertEqual(city.name, name)
        self.assertEqual(city.population, population)
        self.assertEqual(city.demand, demand)
        self.assertEqual(city.plants, plants)
