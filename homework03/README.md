# Homework 03 - 2001: A Space Turbidity

## Homework Scenario & Objective
Homework 03 calls back onto the operation a robotic vechile conducted on Mars, where it investigated five meteorite landings sites. The robot collected samples at these sites and are taking them back to the lab for analysis. However, we need clean water to test them, and as such have developed a script to test the safety of the water, as well as the time it takes for it to become safe to us. Through this, we are implementing our knowledge of JSON librarys to analyize the dataset, as well as implementing proper coding unit testing and docstring communication methods. 

## Scripts & Script Description

1. `water_Safety.py`
Python script that reads in the water quality dataset, and prints out three key pieces of information 
	- The current water turbidity (which is taken as the average of the most recent five data points)
	- Whether that calculated turbidity value is below a safe threshold
	- The minimum time required for turbidity to fall below the safe threshold (if it is already below the safe threshold, the script would report 0 hours). 

2. `turbidity_data.json`
After downloading the water quality dataset, this JSON dictionary is created with a `turbidity_data` key, whose value is a time series list of dictionaries. 

3. `test_water_Safety.py`
A Pytest script to test the validity of the functions of the `water_Safety.py` script. 

## Part 1: Reading in the data set
For reading in the data set, in command-line, type: `curl https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json --ouput my.filename`

This will download the data set under the name `my.filename` that is used for the script. In my script, this file is referred to as: `turbidity_data` in this homework03 directory


## Part 2: Calculating the turbidity of the water samples & minimum time to return to a safe threshold
In the script `water_Safety.py`, there are two functions: turbidity() & timeCalc() 

Turbidity() takes the JSON list and parses through for specific values needed to calculate the turbidity of the water samples. This value is then challenged against a threshold, which will determine if the water is safe or not. If it is not safe, the timeCalc() function is called. 

timeCalc() takes the turbidity value calculated previously and calculates the amount of time needed to return the water to safer conditions. 

This information is outputted on the command-line


## Running and Interpreting the script


To run this script, you must first run the `curl` command noted above to download the data set which this script currently uses. 

Then type the command `python3 water_Safety.py`, which will print out the conclusion for safety for each water sample taken. 

You will see a long list of information similar to that of:

```
    Average turbidity based on most recent five measurements = 1.1992 NTU

    Warning: Turbidity is above threshold for safe use

    Minimum time required to return below a safe threshold = 8.99 hours 
```

```
    Average turbidity based on most recent five measurements = 0.9852 NTU

    Info: Turbidity is below threshold for safe use

    Minimum time required to return below a safe threshold = 0 hours

```
The first line outputs the 5 most recent water measurements taken and their turbidity value. A value between 0.2 and 1.6 is to be expected (in NTU units). If the value is <1, the water is safe. If the value is 1<, it is unsafe to use. The second line indicates whether the water is safe to use or not. If the water is deemed not safe to use, like that in example 1), a third line is ouputted, which indicates how long it will for it to be safe. 


