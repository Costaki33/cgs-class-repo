import json 
import logging
from typing import List 
import socket
import numpy as np 
import math 
logging.basicConfig(level=logging.DEBUG)

def turbidity(a_dictionary: list) -> float:
    
    '''
    This 'turbidity' function takes the imported JSON file and outputs the average turbidity for the last 5 
    measurements taken, as well as whether or not the water is safe to use under a certain threshold. 

    Turbidity is calculated by: T = a0 * I90, where:
    T = Turbidity in NTU Units (0 – 40)
    a0 = Calibration constant
    I90 = Ninety degree detector current

    The a0 and I90 variables are pulled from the JSON file    


    Args:
        a_dictionary (list) : expect a dictionary (aka the JSON data set) 

    Returns:
        T : the average turbidity value calculated 

    '''
    t_temp = 0
    b = 0

    
    for item in range(len(a_dictionary)):
        a0 = a_dictionary[item]['calibration_constant']
        I90 = a_dictionary[item]['detector_current']

        t_temp += (a0 * I90)   
   

    T = t_temp / 5  
   
    print('average turbidity from last 5 measurments =', T, 'NTU')  
    
    if (T < 1.0):
        safetyStatus = logging.info(" The water quality is safe")
        print("Minimum time required to return below a safe threshold = 0 hours\n")   
    elif(T > 1.0):
        safetyStatus = logging.warning(" Turbidity is ABOVE threshold for safe use")
        b = timeCalc(T)
        print("Minimum time required to return below a safe threshold =", b, "hours", "\n")

    return T
    


def timeCalc(T: float) -> float:
  
    '''
    This 'timeCalc' function calculates the minimum time to return below a safe threshold - being 1.0 
    
    Taking this equation: Ts > T0(1-d)**b, where:
    Ts = Turbidity threshold for safe water
    T0 = Current turbidity
    d = decay factor per hour, expressed as a decimal
    b = hours elapsed

    The equation below solves for b, the time elapsed before the sample is below the safe threshold
 
    '''
    Ts = 1.0 # threshold for safe water to use 
    T0 = T
    d = 0.02  

    b = np.log((Ts/T0)) / np.log((1-d)) 
    return b

    

    

def main():
  
    with open('turbidity_data.json', 'r') as f:
        turb_data = json.load(f)

    turb_data = list(turb_data['turbidity_data'])
    
    for i in range(0, len(turb_data), 5):
        dataset = turb_data[i: i+5]
        T = turbidity(dataset)
        b = timeCalc(T)        

     
    return

if __name__ == '__main__':
    main()
    

