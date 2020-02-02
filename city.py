from typing import Iterable

from power import PowerPlant


class City:
    def __init__(
        self, name: str, population: int, demand: int, plants: Iterable[PowerPlant]
    ):
        self.name = name
        self.population = population
        self.demand = demand
        self.plants = plants
