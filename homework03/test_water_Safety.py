import pytest
from water_Safety import timeCalc
from water_Safety import turbidity

'''
Unit testing for each of the functions:
    timeCalc()
    turbidity()
'''

def test_timeCalc():
    with pytest.raises(ZeroDivisionError):
        timeCalc(0)
   
    with pytest.raises(TypeError):
        timeCalc('aword')
   
    with pytest.raises(NameError):
        timeCalc(b)
    
    assert isinstance(timeCalc(2), float) == True
      
    assert timeCalc(1) == 0

 
def test_turbidity(): 
    with pytest.raises(KeyError):
        turbidity([{'word': 1}])
   
    with pytest.raises(TypeError):
        turbidity(['word'])
       
    with pytest.raises(TypeError):
        turbidity([{'calibration_constant': 'a', 'detector_current': 1}])
    
    assert turbidity([{'calibration_constant': 1, 'detector_current': 0}]) == 0
    
    assert turbidity([{'calibration_constant': 1, 'detector_current': 2}]) == 0.4
    
