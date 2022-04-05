# Homework 05 - Redis Application with Meteorite Landings Dataset

## Homework 05 Objectives
* Creating a database using Redis to store the meteorite landings data that would save a backup of the database every second 
* Develop a Flask application using Python to both send & recieve the data stored in the database 
* Be able to request data in a dataset (in this case Metoerite Landing data) using a Flask application

## Dataset Description
1. `Meteorite_Landings.json`: This dataset contains all of the meteorite landing sites and their associated datapoints, stored as a list of dictionaries, such as:
    - Mass
    - Geographic location
    - Class type of the meteorite at a specific landing site

## Reviewing the Scripts
1. `app.py`: This script contains the Flask routes that the user can use to both send & recieve data as such: 
    - This script contains a `POST` method, which will load the Meteorite Dataset into a Redis database instance
    - This script contains a `GET` method, which outputs the dataset in the terminal

## Building The Image
Run the following commands in a terminal shell (EX. Powershell, CMD, etc.):
  1. Clone this repository using the `git clone` command:
    - The following should be on your local machine:
        ```
        [costaki@isp02 homework05]$ ls
        app.py  Dockerfile  Makefile  README.md startCriteria.txt
        ```
  2. Download the Meteorite Landings Dataset:
    - `curl https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json --output Meteorite_Landings.json`
  3. Now, build the image
    - `docker build -t <your username>/meteorite-data-cgs:1.0 .` 
    - Note: replace `<your username>` with your docker username

  4. Start the Redis container
    - `docker run -d -p <your redis port number>:6379 -v $(pwd)/data:/data:rw --name=<container name>-redis redis:6 --save 1 1`
    - For instance, it shoud look like this:
        ```
        [costaki@isp02 homework05]$ docker run -d -p 6431:6379 -v $(pwd)/data:/data:rw --name=costaki-redis redis:6 --save 1 1
        5f7d7e2f1dc68feafe0455e0c49566e84299303e8a2bc510e3f2c6c1d5f8c9f6
        ```
    - The long string of numbers and letters is the specific ID of this specific Redis container

  5. Start the Flask container
    - `docker run --name "meteorite-data-cgs" -d -p <your flask port number>:5000 costaki33/meteorite-data-cgs:1.0`
    - For Example, your command should look like this:
        ```
        [costkai@isp02 homework05]$ docker run --name "meteorite-data-cgs" -d -p 5031:5000 costaki33/meteorite-data-cgs:1.0
        ```
    - A string will pop up again, this being the ID of the Flask container 

6. Find the specific IP Address that connects the two containers (Flask & Redis)
    - `docker inspect <redis container id> | grep IPAddress`
    - It is important to note, back at step 4, to recall the string ID, you will copy it into the <redis container ID> space 
    - However, if you forgot your redis container ID, no worries! You can run `docker ps -a | grep <redis container name>`
           - For Example:
               ```
               [costaki@isp02 homework05]$ docker ps -a | grep costaki-redis
        5f7d7e2d1dc   redis:6                                   "docker-entrypoint.s…"   1 hour ago    Up 2 hours                0.0.0.0:6438->6379/tcp, :::6438->6379/tcp   costaki-redis
               [costaki@isp02 homework05]$ docker inspect bb665e716631 | grep IPAddress
               ```
    - From the output sequence, we can determine that the IP Address that connects the Flask & Redis containers is: `172.17.0.23`

7. Open the `app.py` using the `VIM` service:
    - `vim app.py` to navigate into the Python script
    - Set the `host` variable to the newly discovered IP Address as follows:
        ```
        ...
        def call_redis_client()
            return redis.Redis(host = '172.17.0.23', port = 6379, db = 0)
        ...
        ```
You are now all set up to use the application! 

## Interpreting the Results

There are three types of specified commands the user can utilize to interact with this application, which are highlighted below:


  1. This POST command loads the data into the Redis container
      `curl -X POST localhost:<your flask port number>/data` to load the data into the Redis container
      - For Example:
      ```
      [costaki@isp02 homework05]$ curl -X POST localhost:5031/data
        [INFO]: Successfully uploaded the dataset
      ```
      
  2. This GET command outputs all the data in the Meteorite Landings Dataset
      `curl -X GET localhost:<your flask port number>/data` to output all of the data in the dataset
      - For Example:
     ```
      [costaki@isp02 homework05]$ curl -X GET localhost:5031/data
      [
          {
            "GeoLocation": "(26.4043, -78.3046)",
            "id": "10111",
            "mass (g)": "496",
            "name": "Lisa",
            "recclass": "H6",
            "reclat": "26.4043",
            "reclong": "-78.3046"
           },
          {
            "GeoLocation": "(-86.2178, 12.3718)",
            "id": "10064",
            "mass (g)": "4605",
            "name": "Hilma",
            "recclass": "H4",
            "reclat": "-86.2178",
            "reclong": "12.3718"
          }
      ]
      ```
      - From the example output above, we can see all the entries in the dataset in JSON format
 
   3. This GET command queries a specific index in the data set
        `localhost:<your flask port number>/data?start=<starting index> -X GET`
      - For Example:
      ```
      [costaki@isp02 homework05]$ curl -X GET localhost:5031/data?start=21 -X GET
      [
          {
           "GeoLocation": "(26.4043, -78.3046)",
           "id": "10111",
           "mass (g)": "496",
           "name": "Lisa",
           "recclass": "H6",
           "reclat": "26.4043",
           "reclong": "-78.3046"
          },
         {
           "GeoLocation": "(-86.2178, 12.3718)",
           "id": "10064",
           "mass (g)": "4605",
           "name": "Hilma",
           "recclass": "H4",
           "reclat": "-86.2178",
           "reclong": "12.3718"
          } 
      ]
      ```
Happy data hunting!
