from numbers import Real
from typing import Union, List, Tuple

from power import PowerPlant
from util import validate_nonnegative_real


class City:
    def __init__(
        self,
        name: str,
        population: int,
        demand: Real,
        plants: Union[List[PowerPlant], Tuple[PowerPlant]],
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

    def to_dict(self):
        return {
            "name": self.name,
            "population": self.population,
            "demand": self.demand,
            "available_capacity": self.available_capacity,
            "plant_count": len(self.plants),
        }
