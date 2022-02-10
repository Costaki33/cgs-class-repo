import math
import json
import random 

'''

Below is the code for readin_generator.py

The calc_gcd is an algorithm that uses the great-circle distance algorithm that calcualtes the distance between points 

This is used to claculate the distance between different sites, which is used to calculate the travel time

The for loop below iterates through the .json file we develoepd with generator.py, seeking for different compositiosn to add to the
total travel time.


'''





# The second Python script should use the json library to read in the data generated in part 1 and store it as a dictionary
with open('dataSet.json', 'r') as f:
    ml_data = json.load(f)

mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

# stony time - 1 hr
# iron time - 2 hr
# stony-iron - 3 hrs 

ROB_SPEED = 10 # robot speed in km/h
INIT_LAT = 16.0
INIT_LON = 82.0



sites_list = ml_data["sites"]
counter = 0
total_time = 0.0


for i in sites_list:
    dist = calc_gcd(INIT_LAT, INIT_LON, i["latitude"], i["longitude"])
        
    travel_time = dist / ROB_SPEED

    if i["composition"] == "stony":
        timeAtMeteorite = 1 
    elif i["composition"] == "iron":
        timeAtMeteorite = 2 
    elif i["composition"] == "stony-iron":
        timeAtMeteorite = 3 

    print('leg ', i["site_id"], ', time to travel = ', travel_time, 'hr, time to sample = ', timeAtMeteorite, "hr")
    counter += 1
    total_time += (travel_time + timeAtMeteorite) 

print('number of legs = ', counter, 'total time elapsed = ', total_time, 'hr')  









