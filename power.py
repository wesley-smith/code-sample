from enum import Enum


class PowerCategories(Enum):
    """
    Major power categories according to the US EIA:

    https://www.eia.gov/energyexplained/electricity/electricity-in-the-us.php
    """

    FOSSIL = "FOSSIL"
    NUCLEAR = "NUCLEAR"
    RENEWABLE = "RENEWABLE"


class PowerPlant:
    def __init__(self, capacity: int, category: str):
        sanitized_category = category.upper()
        if not PowerCategories.__members__.__contains__(sanitized_category):
            raise ValueError(
                f'Expected "{category}" to be one of {", ".join(item[0] for item in PowerCategories.__members__.items())}'
            )
        self.capacity = capacity
        self.category = sanitized_category
