import json

from city import City
from power import (
    NuclearPlant,
    WindPlant,
    FossilPlant,
    SolarPlant,
)


def main():
    with open("cities.json") as f:
        input_cities = json.load(f)

    cities = []
    for city in input_cities:
        plants = []
        for plant in city["power_plants"]:
            category = plant.get("category", "")
            if category == "fossil":
                plants.append(FossilPlant(plant["subcategory"], plant["capacity"]))
            elif category == "nuclear":
                plants.append(
                    NuclearPlant(plant["reactor_count"], plant["reactor_capacity"])
                )
            elif category == "renewable":
                subcategory = plant.get("subcategory", "")
                if subcategory == "solar":
                    plants.append(SolarPlant(plant["area"], plant["efficiency"]))
                elif subcategory == "wind":
                    plants.append(
                        WindPlant(plant["turbine_count"], plant["turbine_rating"])
                    )
                else:
                    raise ValueError(
                        f"{city['name']}: Unknown subcategory for plant: {plant}"
                    )
            else:
                raise ValueError(f"{city['name']}: Unknown category for plant: {plant}")
        cities.append(City(city["name"], city["population"], city["demand"], plants))

    print(cities)


if __name__ == "__main__":
    main()
