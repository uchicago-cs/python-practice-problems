
def out_of_range(x, lb, ub):
    """ Is x outside the range lb to ub (inclusive)?"""

    ### EXERCISE 2 -- YOUR CODE GOES HERE
    # Replace "None" with the correct expression
    r = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return r


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_out_of_range(x, lb, ub, expected):
    recreate_msg = utils.gen_recreate_msg("out_of_range", *(x, lb, ub))

    actual = out_of_range(x, lb, ub)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_out_of_range_1():
    do_test_out_of_range(x=5, lb=3, ub=10, expected=False)


def test_out_of_range_2():
    do_test_out_of_range(x=15, lb=3, ub=10, expected=True)


def test_out_of_range_3():
    do_test_out_of_range(x=3, lb=3, ub=10, expected=False)


def test_out_of_range_4():
    do_test_out_of_range(x=10, lb=3, ub=10, expected=False)
