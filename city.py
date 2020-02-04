from numbers import Real
from typing import Iterable

from power import PowerPlant
from util import validate_nonnegative_real


class City:
    def __init__(
        self, name: str, population: int, demand: Real, plants: Iterable[PowerPlant]
    ):
        self.name = name
        validate_nonnegative_real(population)
        self.population = population
        validate_nonnegative_real(demand)
        self.demand = demand
        self.plants = plants

    @property
    def available_capacity(self) -> Real:
        return sum(plant.capacity for plant in self.plants)
