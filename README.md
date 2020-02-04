# Python Code Sample

This is a code sample written for Oak Ridge National Laboratory, inspired by [this example](https://github.com/ornl-training/code-sample-examples). The intended outcome is to provide a view into what my Python code typically looks like, not necessarily to provide a useful system in any way. As requested, OOP methods will be  emphasized.

## Motivation
I'm especially attracted to some of the research areas ORNL supports - specifically clean energy and astronomy/astrophysics. As such, I decided to follow one of these areas with my sample. Similar to [one of my OMSCS projects](https://wesley-smith.github.io/portfolio/2-climate/), which used real-world climate and energy data, here, I'll be using "fake-world" energy data to produce some "analysis" of the energy mix of a few fictitious cities.

## Description
A `PowerPlant` base class acts as an interface that must be implemented by subclasses. Each subclass represents a type of power generation plant. The main abstraction here is that each plant type has its own way of defining its output `capacity`.

The `City` class contains some general data for the city as well as a list of power plants capable of serving the city. It uses this list to aggregate data regarding its energy mix.

Numerous simplifying assumptions about power generation are made. Chief among these assumptions is that plant capacity and city demand are constants. In reality, these are highly variable with time.

Finally, a script is made available in `main.py` which loads in sample data and instantiate these classes. The data is then loaded to a pandas `DataFrame` for some simple analysis.

## Installation

This code was written in Python 3.6, but should work with any Python 3.5 or greater.

Ensure that dependencies are installed by running the following command (within a `virtualenv`, if desired):

```
pip install -r requirements.txt
```

## Running the code

From the root project directory, run the analysis with:

```
python main.py
```

Optionally, you may pass an alternate input file name using the `-i`/`--input_file` option (run with `-h` for details).

From the same directory, the tests can be run with:

```
python -m unittest discover -vs test
```

## Example output
|    | name       |   population |   demand |   available_capacity |   plant_count |   demand_per_capita |   pct_demand_satisfied |
|---:|:-----------|-------------:|---------:|---------------------:|--------------:|--------------------:|-----------------------:|
|  0 | Fooville   |       500000 |  1000000 |            1.077e+06 |             5 |                   2 |                  107.7 |
|  1 | Barborough |      1000000 |  1000000 |            1.945e+06 |             7 |                   1 |                  194.5 |
