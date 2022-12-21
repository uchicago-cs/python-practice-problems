def compute_matching_indices(x, y):
    """
    Returns a new array consisting of the indices where
    x == y.
    Input: 
        x: 1-dimensional array
        y: 1-dimensional array
    Returns: a sorted array of the indices where x[i] == y[i]
    Note that the returned array must be one-dimensional! 
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

def test_compute_matching_indices():

    x = np.array([1, 2, 3, 4])
    y = np.array([1, 5, 3, 2])

    recreate_msg = utils.gen_recreate_msg('compute_matching_indices', x, y)
    
    result = compute_matching_indices(x, y)

    utils.check_none(result, recreate_msg)
    utils.check_is_ndarray(result, recreate_msg)
    utils.check_dtype(result, int, recreate_msg)
    
    utils.check_array_equal(result, np.array([0, 2]), recreate_msg)