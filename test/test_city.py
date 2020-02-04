from random import randrange
from unittest import TestCase
from unittest.mock import Mock

from city import City
from power import NuclearPlant


class CityTest(TestCase):
    def test_constructor(self):
        name = "Fooville"
        population = 10_000
        demand = 100_000_000
        plants = (NuclearPlant(1, 1),)
        city = City(name, population, demand, plants)
        self.assertEqual(city.name, name)
        self.assertEqual(city.population, population)
        self.assertEqual(city.demand, demand)
        self.assertEqual(city.plants, plants)

    def test_available_capacity(self):
        plant_count = 5
        plant_capacities = [randrange(10_000, 1_000_000) for _ in range(plant_count)]
        total_capacity = sum(plant_capacities)
        mock_plants = [Mock(capacity=capacity) for capacity in plant_capacities]
        city = City(name="Bar City", population=1, demand=1, plants=mock_plants)
        self.assertEqual(city.available_capacity, total_capacity)
