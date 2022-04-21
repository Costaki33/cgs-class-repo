# Kubernetes-Based (k8's) Deployment for Meteorite Landings Database Server Application 
This project used Kubernetes (k8s) to deploy a test environment that allows the user to interact with a Flask web application using a Redis database both to load and receive a meteorite dataset containing specific information about meteors sighted by the Meteorical Society. These meteorite features include: class, longitude, latitude, and mass (g). 

The scripts for this project include:
- ```Dockerfile```: This script downloads all the necessary dependencies and environment variables for the developed Flask application
- ```app.py```: This script provides routes to both download and return the specified Meteorite Landings dataset
Additionally, there are five ```.yml files,``` which when used on a Kubernetes cluster create a environment needed to interact with this API:
- ```costaki-test-redis-pvc.yml```: This script stores the data written to it from the -deployment file- independently from the pods
- ```costaki-test-redis-deployment.yml```: This script creates a deployment for the Redis database that is utilized 
- ```costaki-test-redis-service.yml```: This script provides a -persistent- IP address that is able to interacted with using Redis
- ```costaki-test-flask-deployment.yml```: This script creates a deployment with two replicas for the Flask API that is utilized
- ```costaki-test-flask-service.yml```: This script provides a persistent IP address that is able to interact with the API when utilized

## Running in Kubernetes
After logging into your Kubernetes cluster, apply a configuration of all ```.yml files``` use the following command for each of the 5 ```yml``` files:
``` bash
[funky@mnky ~]$ kubectl apply -f <file name>
```
In addition, make sure your Python-based debug file has been configured as well. 

This action creates various k8 resources for each file type of the following:  ```pvc```, ```pods```, ```deployments```, and ```services```. You can check the IDs of these resources, execute the following command:
``` bash
[funky@mnky ~]$ kubectl get all -o wide
```
You can find the IP address of your Flask service, which you will need which you exec into your debug file, with:
``` bash
[funky@mnky ~]$ kubectl get services
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
costaki-test-flask-service   ClusterIP   10.106.22.192    <none>        5000/TCP   8h
```
Now execute the following command to exec into your Python-based debug pod with:
``` bash
[funky@mnky ~]$ kubectl exec -it <python-debug-ID> /bin/bash
root@trunk-debug-deployment-6fd6c5886b-qsxz4:/#
```
Now, you're in the debug pod! You can access the Flask API with the service's IP address and the port ```5000``` by using ```curl``` to the route with ```/data```. First, load the data with the ```-X POST```  command, now you can retrieve the dataset without having to write ```GET``` as in the previous project.
``` bash
root@trunk-debug-deployment-6fd6c5886b-qsxz4:/# curl -X POST 10.106.22.192:5000/data
-Data has been loaded-
root@trunk-debug-deployment-6fd6c5886b-qsxz4:/# curl 10.106.22.192:5000/data
[
 {
  "name": "Agnes",
  "id": "10298",
  "recclass": "H6",
  "mass (g)": "801",
  "reclat": "-61.5820",
  "reclong": "-10.3998",
  "GeoLocation": "(-61.5820, -10.3998)"
 },
 {
  "name": "Jennifer",
  "id": "10299",
  "recclass": "L5",
  "mass (g)": "539",
  "reclat": "-84.0579",
  "reclong": "69.9994",
  "GeoLocation": "(-84.0579, 69.9994)"
 },
 {
  "name": "Christina",
  "id": "10300",
  "recclass": "H5",
  "mass (g)": "4291",
  "reclat": "-38.1533",
  "reclong": "-46.7127",
  "GeoLocation": "(-38.1533, -46.7127)"
 }
]
```
Now, you can retrieve your data! Happy data mining!
