from abc import ABC, abstractmethod
from enum import Enum
from numbers import Real

from util import validate_nonnegative_real, sanitize_str_enum_value


class PowerCategories(Enum):
    """
    Major power categories according to the US EIA:

    https://www.eia.gov/energyexplained/electricity/electricity-in-the-us.php
    """

    FOSSIL = "FOSSIL"
    NUCLEAR = "NUCLEAR"
    RENEWABLE = "RENEWABLE"


class FossilCategories(Enum):
    """A (non-exhaustive) set of fossil fuel categories"""

    COAL = "COAL"
    NATURAL_GAS = "NATURAL GAS"


class RenewableCategories(Enum):
    """A (non-exhaustive) set of renewable categories"""

    WIND = "WIND"
    SOLAR = "SOLAR"


class PowerPlant(ABC):
    """
    A parent class for power plants of various generation types. Child classes must
    implement the `category` and `capacity` properties.
    """

    @property
    @abstractmethod
    def category(self) -> str:
        pass

    subcategory = None  # Subclasses can override if needed

    @property
    @abstractmethod
    def capacity(self) -> Real:
        pass


class NuclearPlant(PowerPlant):
    def __init__(self, reactor_count: int, reactor_capacity: Real):
        self.reactor_count = reactor_count
        self.reactor_capacity = reactor_capacity

    @property
    def category(self) -> str:
        return PowerCategories.NUCLEAR.value

    @property
    def capacity(self) -> Real:
        return self.reactor_capacity * self.reactor_count


class FossilPlant(PowerPlant):
    def __init__(self, subcategory: str, capacity: Real):
        validate_nonnegative_real(capacity)
        self.capacity_ = capacity
        self.subcategory = sanitize_str_enum_value(subcategory, FossilCategories)

    @property
    def category(self) -> str:
        return PowerCategories.FOSSIL.value

    @property
    def capacity(self) -> Real:
        return self.capacity_


class WindPlant(PowerPlant):
    subcategory = RenewableCategories.WIND.value

    def __init__(self, turbine_count: int, turbine_rating: Real):
        validate_nonnegative_real(turbine_count)
        validate_nonnegative_real(turbine_rating)
        self.turbine_count = turbine_count
        self.turbine_rating = turbine_rating

    @property
    def category(self) -> str:
        return PowerCategories.RENEWABLE.value

    @property
    def capacity(self) -> Real:
        return self.turbine_count * self.turbine_rating


class SolarPlant(PowerPlant):
    subcategory = RenewableCategories.SOLAR.value

    def __init__(self, area: Real, efficiency: Real):
        validate_nonnegative_real(area)
        validate_nonnegative_real(efficiency)
        self.area = area
        self.efficiency = efficiency

    @property
    def category(self) -> str:
        return PowerCategories.RENEWABLE.value

    @property
    def capacity(self) -> Real:
        return self.area * self.efficiency
