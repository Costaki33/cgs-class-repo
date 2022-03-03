
from ml_data_analysis import check_hemisphere, compute_average_mass, count_classes
import pytest

def test_check_hemisphere():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert check_hemisphere(10, 10) == 'Northern & Eastern' 
    assert isinstance(check_hemisphere(10,10), str) == True 
    with pytest.raises(ValueError):
        check_hemisphere(0,0) 


def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a':3}], 'a') == 2
    assert isinstance(compute_average_mass([{'a':1}, {'a':2}, {'a':3}], 'a'), float) == True
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a':1}], 'c')
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')


def test_count_classes():
    assert count_classes([],'') == {}
    assert count_classes([{'a': 'class1'}, {'a': 'class1'}, {'a': 'class1'}], 'a') == {'class1': 3}
    assert count_classes([{'a': 'hello'}, {'a': 'bye'}, {'a': 'hello'}], 'a') == {'hello':2, 'bye':1}
    with pytest.raises(KeyError):
        count_classes([{'a': 1}, {'a':'hi'}], 'wrong')
