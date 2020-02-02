from unittest import TestCase

from power import PowerPlant, PowerCategories


class PowerPlantTest(TestCase):
    def test_constructor(self):
        capacity = 10000
        category = PowerCategories.FOSSIL.value

        with self.subTest("power categories are case-insensitive"):
            plant_1 = PowerPlant(capacity, "FOSSIL")
            plant_2 = PowerPlant(capacity, "fossil")
            self.assertEqual(plant_1.capacity, capacity)
            self.assertEqual(plant_1.category, category)
            self.assertEqual(plant_2.capacity, capacity)
            self.assertEqual(plant_2.category, category)

        with self.subTest("invalid categories produce an error"):
            with self.assertRaises(ValueError) as handler:
                PowerPlant(capacity, "foo")

            self.assertEqual(
                handler.exception.args[0],
                'Expected "foo" to be one of FOSSIL, NUCLEAR, RENEWABLE',
            )
