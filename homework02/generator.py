import json 
import random 
import math 
import numpy as np

# Generate five random pairs of latitiude (btwn 16.0 - 18.0) degrees North and longitudes (btwn 82.0 - 84.0) degrees East
# in decimal notation

# A list of meteorite compositions 
meteoriteComposition = ["stony", "iron", "stony-iron"]

siteList = []

# randomly generate 5 coordiantes as mentioned above
for i in range(5):
    
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











