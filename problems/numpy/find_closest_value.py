def find_closest_value(x):
    """
    Returns the index and corresponding value in the one-dimensional 
    array x that is closest to the mean 
    Examples:
    find_closest_value(np.array([1.0, 2.0, 3.0])) -> (1, 2.0)
    find_closest_value(np.array([5.0, 1.0, 8.0])) -> (0, 5.0)
    Inputs: 
        x: 1-dimensional array of values
    Returns: the index and the scalar value in x that is 
        closest to the mean
    """
    
    # YOUR CODE HERE
    # Replace None with an appropriate return value
    return None
    

#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
import numpy as np
sys.path.append('../')

import test_utils as utils

def test_find_closest_value():

    def manual_closest_value(x):
        closest_delta = 1e9
        
        closest_idx = None
        closest_val = None
        
        for i, x_item in enumerate(x):
            delta = abs(x_item - np.mean(x))

            if delta < closest_delta:
                closest_delta = delta
                closest_idx = i
                closest_val = x_item
        assert closest_idx is not None
        
        return closest_idx, closest_val
        
    
    x = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5])

    recreate_msg = utils.gen_recreate_msg('find_closest_value', x)

    result = find_closest_value(x)

    utils.check_none(result, recreate_msg)

    expected_closest_val = manual_closest_value(x)

    assert expected_closest_val == result, \
        "\n function returned {} as closest val ".format(result) \
        + "but we expected {}\n\n".format(expected_closest_val) \
        + recreate_msg
