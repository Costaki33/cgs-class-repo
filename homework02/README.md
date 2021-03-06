# Homework 02 - Return of the JSON

## Homework Scenario
In this homework, the given scenario is you are operating a robotic vechile on Mars and are tasked to investigate five meteorite landing sites in Syrtis Major.

## Homework Objective
The project objective for this homework exercise is to investiage different potential landing sites a robotic vechile I am operating on Mars may encounter by maping different potential meteorite sites and the characteristics that go along with them (such as composition, latitude, longitude, distance travelled, and time traveled). This means we can have a rough estimate of how far most meteorite sites are from each other on Mars due to our set latitude/longitude bounds, as well as the total mission exploration and travel time. 

## Scripts
In this folder, there are several files:
1. `dataSet.json`
2. `generator.py`
3. `readin_generator.py`
4. `README.md`

## Script Descriptions
Below are descriptions of each of the files in this folder:

1. `dataSet.json`: 
`dataSet.json` is a file that is created everytime `generator.py` is run. It is where the dictionary is stored and can be called onto.

2. `generator.py`:
`generator.py` creates random latitude and longitude values between a set of predeterminded bounds, as well as randomly selects a type of meteorite crator, which is stored under an id that can be called up through a dictionary.

3. `readin_generator.py`:
`readin_generator.py` parses through `dataSet.json` and calculates the total travel time of the mission, as well as time it takes to sample the meteorite.  


## Instructions
To run the code, please type `python3 generator.py`, followed by `python3 readin_generator.py`. You will see no output by `generator.py` but will see an output with `readin_generator.py`. 

As per how to interpret the data, a lower total travel time means that the crators are close to each other. Expect values around 45-53 total hours. 











