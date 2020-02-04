from enum import Enum
from numbers import Real
from typing import Type


def sanitize_str_enum_value(value: str, enum_cls: Type[Enum]) -> str:
    """
    Performs a case-insensitive search to ensure `value` is in `enum_`.

    :return sanitized value according `enum_`
    """
    upper_value = value.upper()
    for member in enum_cls:
        if member.value.upper() == upper_value:
            return member.value

    raise ValueError(
        f'Expected "{value}" to be one of {", ".join(member.value for member in enum_cls)}'
    )


def validate_nonnegative_real(number: Real):
    if not isinstance(number, Real) or number < 0:
        raise ValueError(f"{number} must be a non-negative real number")
