import json 
import random 
import math 
import numpy as np

'''
This script generates a random latitude, longitude, and compositoin for 5 meteorite landing sites 

   meteortieCompositon is a list that has three differnet compositions for each of the meteorites our robot is landing on:
      - stony
      - iron
      - stony-iron

   The for loop iterates for the request 5 landing sites, and generates a latitude and longitude value from the ranges of 
   lat(16.0 - 18.0) and long(82.0, 84.0) randomly using a random number generator from Python

   We create a dictionary called meteoriteData and these values discussed above are made into keys

   The develoepd JSON file is exported out 

'''




# Generate five random pairs of latitiude (btwn 16.0 - 18.0) degrees North and longitudes (btwn 82.0 - 84.0) degrees East
# in decimal notation

# A list of meteorite compositions 
meteoriteComposition = ["stony", "iron", "stony-iron"]

siteList = []

# randomly generate 5 coordiantes as mentioned above

for i in range(1, 6):
    
    latitude = np.random.uniform(16.0, 18.0)
    longitude = np.random.uniform(82.0, 84.0)

    composition = random.choice(meteoriteComposition)


    meteoriteData = {}

    meteoriteData["site_id"] = i 
    meteoriteData["latitude"] = latitude  
    meteoriteData["longitude"] = longitude
    meteoriteData["composition"] = composition       

    siteList.append(meteoriteData)

# save the data into a JSON file 
sitesData = {"sites": siteList}

coordinateDataset = json.dumps(sitesData, indent = 4)

# this will export the json dataset as a file that can be called in part 2
with open ('dataSet.json', 'w') as outfile:
    outfile.write(coordinateDataset)











