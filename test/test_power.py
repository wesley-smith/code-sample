from unittest import TestCase

from power import PowerPlant


class PowerPlantTest(TestCase):
    def test_constructor(self):
        capacity = 10000
        fuel_type = 'fossil'
        plant = PowerPlant(capacity, fuel_type)

        self.assertEqual(plant.capacity, capacity)
        self.assertEqual(plant.fuel_type, fuel_type)
