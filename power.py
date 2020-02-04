from abc import ABC, abstractmethod
from enum import Enum
from numbers import Real


class PowerCategories(Enum):
    """
    Major power categories according to the US EIA:

    https://www.eia.gov/energyexplained/electricity/electricity-in-the-us.php
    """

    FOSSIL = "FOSSIL"
    NUCLEAR = "NUCLEAR"
    RENEWABLE = "RENEWABLE"


class PowerPlant(ABC):
    """
    A parent class for power plants of various generation types. Child classes must
    implement the `capacity` property.
    """

    def __init__(self, category: str):
        """
        :param category: must match a major power category (case-insensitive)
        """
        sanitized_category = category.upper()
        if not PowerCategories.__members__.__contains__(sanitized_category):
            raise ValueError(
                f'Expected "{category}" to be one of {", ".join(item[0] for item in PowerCategories.__members__.items())}'
            )
        self.category = sanitized_category

    @property
    @abstractmethod
    def capacity(self) -> Real:
        raise NotImplementedError("Subclasses must implement this property")
