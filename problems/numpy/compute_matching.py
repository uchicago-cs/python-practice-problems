def compute_matching(x, y):
    """
    Returns a new array which is "true" everywhere x == y and 
    false otherwise. 
    Input:
        x: n-dimensional array
        y: n-dimensional array
    Returns: Boolean-valued n-dimensional array with the same shape as 
             x and y
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

def test_compute_matching_values():

    x = np.array([1, 2, 3, 4])
    y = np.array([1, 5, 3, 2])

    recreate_msg = utils.gen_recreate_msg('compute_matching', x, y)
    
    result = compute_matching(x, y)

    utils.check_none(result, recreate_msg)
    utils.check_is_ndarray(result, recreate_msg)
    utils.check_dtype(result, bool, recreate_msg)
        
    
    utils.check_array_equal(result, np.array([True, False, True, False]),
                            recreate_msg)