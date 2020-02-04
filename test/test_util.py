from enum import Enum
from unittest import TestCase

from util import sanitize_str_enum_value, validate_nonnegative_real


class TestEnum(Enum):
    FOO = "FOO"
    BAR = "bar"


class TestUtil(TestCase):
    def test_sanitize_string_enum_value(self):
        for test_value in ("foo", "Foo", "fOo"):
            self.assertEqual(
                sanitize_str_enum_value(test_value, TestEnum), TestEnum.FOO.value
            )

        for test_value in ("BAR", "Bar", "BaR"):
            self.assertEqual(
                sanitize_str_enum_value(test_value, TestEnum), TestEnum.BAR.value
            )

        with self.assertRaises(ValueError) as handler:
            sanitize_str_enum_value("unknown", TestEnum)

        self.assertEqual(
            handler.exception.args[0], 'Expected "unknown" to be one of FOO, bar',
        )

    def test_validate_nonnegative_real(self):
        valid_values = (0, 0.0, -0.0, 0.1, 10, 10.0)
        invalid_values = (-0.1, -1, -10, -10.0, "100", {"value": "100"})

        for val in valid_values:
            with self.subTest(value=val):
                validate_nonnegative_real(val)

        for val in invalid_values:
            with self.subTest(value=val):
                self.assertRaises(ValueError, validate_nonnegative_real, val)
