from unittest import TestCase

from power import PowerCategories, NuclearPlant

        with self.subTest("invalid categories produce an error"):
            with self.assertRaises(ValueError) as handler:
                PowerPlant("foo")

            self.assertEqual(
                handler.exception.args[0],
                'Expected "foo" to be one of FOSSIL, NUCLEAR, RENEWABLE',
            )

    def test_capacity_not_implemented(self):
        plant = PowerPlant("fossil")
        with self.assertRaises(NotImplementedError):
            capacity = plant.capacity
