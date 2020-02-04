import random
from unittest import TestCase

from power import (
    PowerCategories,
    NuclearPlant,
    WindPlant,
    RenewableCategories,
    FossilPlant,
    FossilCategories,
    SolarPlant,
)


class NuclearPlantTest(TestCase):
    def test_capacity(self):
        test_count = 5
        for _ in range(test_count):
            reactor_count = random.randint(1, 5)
            reactor_capacity = random.uniform(10_000, 50_000)
            plant = NuclearPlant(reactor_count, reactor_capacity)
            self.assertEqual(plant.category, PowerCategories.NUCLEAR.value)
            self.assertIsNone(plant.subcategory)
            self.assertEqual(plant.capacity, reactor_count * reactor_capacity)


class FossilPlantTest(TestCase):
    def test_input_validation(self):
        self.assertRaises(ValueError, FossilPlant, subcategory="bad", capacity=1)
        self.assertRaises(
            ValueError,
            FossilPlant,
            subcategory=FossilCategories.COAL.value,
            capacity=-1,
        )

    def test_capacity(self):
        capacity = 100
        plant = FossilPlant(FossilCategories.COAL.value, capacity)
        self.assertEqual(plant.capacity, capacity)


class WindPlantTest(TestCase):
    def test_input_validation(self):
        self.assertRaises(ValueError, WindPlant, turbine_count=1, turbine_rating=-1)
        self.assertRaises(ValueError, WindPlant, turbine_count=-1, turbine_rating=1)

    def test_capacity(self):
        test_count = 5
        for _ in range(test_count):
            turbine_count = random.randint(1, 5)
            turbine_rating = random.uniform(10_000, 50_000)
            plant = WindPlant(turbine_count, turbine_rating)
            self.assertEqual(plant.category, PowerCategories.RENEWABLE.value)
            self.assertEqual(plant.subcategory, RenewableCategories.WIND.value)
            self.assertEqual(plant.capacity, turbine_count * turbine_rating)


class SolarPlantTest(TestCase):
    def test_input_validation(self):
        self.assertRaises(ValueError, SolarPlant, area=1, efficiency=-1)
        self.assertRaises(ValueError, SolarPlant, area=-1, efficiency=1)

    def test_capacity(self):
        test_count = 5
        for _ in range(test_count):
            area = random.randint(1000, 5000)
            efficiency = random.uniform(5, 10)
            plant = SolarPlant(area, efficiency)
            self.assertEqual(plant.category, PowerCategories.RENEWABLE.value)
            self.assertEqual(plant.subcategory, RenewableCategories.SOLAR.value)
            self.assertEqual(plant.capacity, area * efficiency)
