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
    implement the `category` and `capacity` properties.
    """

    @property
    @abstractmethod
    def category(self) -> str:
        pass

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
