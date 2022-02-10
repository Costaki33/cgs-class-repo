import math
import json
import random 

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

for i in sites_list:
    dist = calc_gcd(INIT_LAT, INIT_LON, sites_list["latitude"], sites_list["longitude"])
        
    travel_time = dist / ROB_SPEED

    if site_list["compositon"] == ["stony"]:
        timeAtMeteorite = 1 
    elif site_list["composition"] == ["iron"]:
        timeAtMeteorite = 2 
    elif site_list["composition"] == ["stony-iron"]:
        timeAtMeteorite = 3 

    print('leg ', site_list["site_id"])











