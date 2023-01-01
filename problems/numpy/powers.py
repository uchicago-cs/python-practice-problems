def powers(N, p):
    """
    Return the first N powers of p. For example:
    powers(5, 2) --> [1, 2, 4, 8, 16]
    powers(5, 4) --> [1, 4, 16, 64, 256]
    Input:
       N: number of powers to return 
       p: base that we are raising to the given powers
    
    Returns: an array consisting of powers of p
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

def test_powers():

    for p in [1, 2, 4]:
        for N in [1, 2, 5, 10]:
            recreate_msg = utils.gen_recreate_msg('powers', N, p)
            
            result = powers(N, p)

            utils.check_none(result, recreate_msg)
            utils.check_is_ndarray(result, recreate_msg)

            utils.check_array_equal(result,
                              np.array([p**i for i in range(N)]),
                              recreate_msg)