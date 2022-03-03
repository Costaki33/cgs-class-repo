# Homework 04 - Meteorite Landings Data Analysis 

This homework assignment compiled a project we had been working in class, which entailed an analyses on the data a rover took fromvarius meteorite landing sites, such as the average mass of meteorites, their location, and the different types of meteorites. 

This homework04 folder includes the following:
- The compiled data set: ```Meteorite_Landing.json```
- A script that outputs a summary of the analysis of the data set: ```ml_data_analysis.py```
- A tester for the summary script: ```test_ml_data_analysis.py```
- A ```Dockerfile``` to run the programs in a container with the required/used base image & dependencies

## Reviewing the Scripts

### Dockerfile
To run the following homework04 scripts in the environment that has the base images/dependencies/install processes/environment variables used when developing the scripts, we will run these scripts in the created ```ml_data_analysis.py``` Docker container.

### Meteorite Landings Data Set: ```Meteorite_Landing.json```
This data set consists of all the unique features of the various meteorite landings provided by The Meteoritical Society. For analysis, I took the class, longitude, latitude, and mass (g) from the dataset.

### Meteorite Landings Data Analysis: ```ml_data_analysis.py```
This script consists of functions that offer a neat compilation of the data set. Specifically, ```ml_data_analysis.py``` outputs information on the meteorites' average mass, number of meteorites per hemisphere, and number of respective class type.

### Meteorite Landings Data Analysis Tester: ```test_ml_data_analysis.py```
This test script tests the accuracy and the functionality of the functions of the meteorite landing data analysis script, ```ml_data_analaysis.py```. Tests include value errors, type & value errors, of various functions. 

#### Pulling & Building a Docker Image
To have a proper functioning image to run these scripts in, you can either pull an existing image from Docker Hub, or build your own. 
To pull the image of these scripts from the Costaki33 Docker Hub repository, run the following command in a terminal shell:  
```bash
[youruser@ex ~]$ docker pull costaki33/ml_data_analysis:hw04 
```
> *Expected output: 
```sh
hw04: Pulling from costaki33/ml_data_analysis
...
```   
To build your own image of the container, run the following command in a terminal shell:
Note, make sure to add the "." at the end of the line as shown below, if not, errors will occur
```sh
[youruser@ex ~]$ docker build costaki33/ml_data_analysis:hw04 .
```
> *Expected output, which should continue for 8 steps: 
```sh
Sending build context to Docker daemon  34.82kB
Step 1/8 : FROM centos:7.9.2009
...
```  
#### Running the Code Inside the Container with an Example Data Set
Run the follow command in terminal shell to enter the costaki33 Docker container:
```sh
[youruser@ex ~]$ docker run --rm -it costaki33/ml_data_analysis:hw04 /bin/bash
```
Once in the container, your user should change from your desktop username to a root user. Here, you will find three scripts listed in the code repository. 
```sh 
[root@9a69274382]# ls/code
```
> Expected output: 
```sh
Meteorite_Landings.json  ml_data_analysis.py  test_ml_data_analysis.py
```
To run the ```ml_data_analysis.py``` script with the provided ```Meteorite_Landings.json``` data set run the following in the container repository.
```sh
[root@9a69274382 code]# ./ml_data_analysis.py Meteorite_Landings.json
```
> The output will be a summary of the following information set:
```bash 
Summary data following meteorite analysis:

Average mass of 30 meteor(s):
83857.3

Hemisphere summary data:
There were 21 meteors found in the Northern & Eastern quadrant
There were 6 meteors found in the Northern & Western quadrant
There were 0 meteors found in the Southern & Eastern quadrant
There were 3 meteors found in the Southern & Western quadrant

 Class summary data:
The L5 class was found 1 times
The H6 class was found 1 times
The EH4 class was found 2 times
The Acapulcoite class was found 1 times
...
```
#### Running the Code inside the Container with a Unique Data Set (Extra Data Set Provided)
Perhaps you would like to run the analysis script against a unique data set besides the example data set provided in the container, you can add your own data set into the pulled container, 

First, exit the container with the ```exit``` command and then run the following command in the repository with your Dockerfile:
```sh
[youruser@ex ~]$ docker run --rm -it -v $PWD:/data costaki33/ml_data_analysis:hw04 /bin/bash
```
This mounts the contents of *your* current directory to a directory *in the* container ```data``` in which you'll be able to access and use your own unique data set. Run the code as discussed above, replacing ```Meteorite_Landings.json``` with the data set you have added to the contianer.

A data set has been provided at this [link](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json) where you can copy it into a file of your own and be utilized. 

#### Running the Tester in the Container
To run ```test_ml_data_analysis.py``` and verify functionality of the program, run the container with the above instructions, move to the code repo and run the following command in a terminal shell:
```sh
[root@9a69274382 code]# pytest test_ml_data_analysis.py
```
> If the analysis script is functioning correctly, it therefore should output 5 passed tests:
```sh +
...                                                                                     [100%]

================================================== 3 passed in 0.04s ===================================================
```
## Final Note: Tester Input
Make sure that the new data set being used against the containerized code resembles that of the ```Meteorite_Landings.json``` data set, where its structure resembles a *dictionary* of one key whose values is a list of dictionaries. 
In addition, make sure that the key strings for mass, latitude, longitude, and class are respectively labeled as ```'mass (g)'```, ```'reclat'```, ```'reclong'```, and ```'recclass'```, as they are the key names the tester and the function are looking for. 
Expected input may look as the following based on your input:
```
{
  "meteorite_landings": [
    {
      "name": "Ruiz",
      "id": "10001",
      "recclass": "L5",
      "mass (g)": "21",
      "reclat": "50.775",
      "reclong": "6.08333",
      "GeoLocation": "(50.775, 6.08333)"
    },
     {
      "name": "Beeler",
      "id": "10002",
      "recclass": "H6",
      "mass (g)": "720",
      "reclat": "56.18333",
      "reclong": "10.23333",
      "GeoLocation": "(56.18333, 10.23333)"
    },

