import argparse
import json

import pandas as pd

from city import City
from power import (
    NuclearPlant,
    WindPlant,
    FossilPlant,
    SolarPlant,
)


def main(args):
    with open(args.input_file) as f:
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

    # Construct a dataframe and do some analysis
    df = pd.DataFrame(data=[city.to_dict() for city in cities])
    df["demand_per_capita"] = df["demand"] / df["population"]
    df["pct_demand_satisfied"] = df["available_capacity"] / df["demand"] * 100

    pd.set_option("display.max_columns", 999)
    pd.set_option("display.width", 999)

    if args.markdown_format:
        print(df.to_markdown())
    else:
        print(df.to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_file",
        type=str,
        help="JSON file containing city data",
        default="cities.json",
    )
    parser.add_argument(
        "-m",
        "--markdown_format",
        help="Default: output is plaintext",
        action="store_true",
    )

    main(parser.parse_args())
