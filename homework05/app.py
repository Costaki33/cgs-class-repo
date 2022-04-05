from flask import Flask, request, jsonify
import redis
import json
from typing import List

app = Flask(__name__)

def call_redis_client():
    
    '''
    
    This function returns the network call where the Flask & Redis containers communicate from 
    
    '''
    return redis.Redis(host = '172.17.0.13', port = 6379, db = 0)

def read_data_from_file() -> List[dict]:

    '''

    This function retrieves the Meteorite Landings data, and returns it as a list of dictionaries

    '''
    dataset = json.load(open('Meteorite_Landings.json', 'r'))
    return dataset['meteorite_landings']

@app.route('/data', methods = ['GET','POST'])
def data():

    '''
    This function loads in the data pulled into a Redis container, if:
    1) The method requested by the user is a POST method request 
        -or-
    2) The funciton returns the data from the dataset if it's a GET method request

    '''

    red = call_redis_client()

    if request.method == 'GET':
        dataset = []
        start = request.args.get('start', 0)
        
        try:
            start = int(start)
            for key in red.scan_iter():
                s = red.hgetall(key)
                s = {key.decode('utf-8'): s[key].decode('utf-8') for key in s.keys()}
                dataset.append(s)
        except ValueError:
            return '[INFO]: Invalid parameter, please make sure the starting parameter is an int\n'
        
        return jsonify(dataset[start:])    
    
    elif request.method == 'POST':
        dataset = read_data_from_file()

        for v in dataset:
            red.hset(v['id'], mapping = v)

        return '[INFO]: Successfully uploaded the dataset \n'    

    return '[ERROR]: Unknown request, try again\n'        

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
