import random
from unittest import TestCase

from power import PowerCategories, NuclearPlant


class NuclearPlantTest(TestCase):
    def test_capacity(self):
        test_count = 5
        for _ in range(test_count):
            reactor_count = random.randint(1, 5)
            reactor_capacity = random.uniform(10_000, 50_000)
            plant = NuclearPlant(reactor_count, reactor_capacity)
            self.assertEqual(plant.category, PowerCategories.NUCLEAR.value)
            self.assertEqual(plant.capacity, reactor_count * reactor_capacity)
