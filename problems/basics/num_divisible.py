def num_divisible(lb, ub, p, q):
    """
    How many numbers between lb and ub (inclusive) are divisible by p
    or divisible by q, but not divisible by both p and q.
    """

    ### EXERCISE 4 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return 


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_num_divisible(lb, ub, p, q, expected):
    recreate_msg = utils.gen_recreate_msg("num_divisible", *(lb, ub, p, q))

    actual = num_divisible(lb, ub, p, q)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_num_divisible_1():
    do_test_num_divisible(lb=1, ub=20, p=2, q=3, expected=10)


def test_num_divisible_2():
    do_test_num_divisible(lb=2, ub=3, p=2, q=3, expected=2)


def test_num_divisible_3():
    do_test_num_divisible(lb=12, ub=20, p=2, q=2, expected=0)


def test_num_divisible_4():
    do_test_num_divisible(lb=1, ub=25, p=3, q=5, expected=11)


def test_num_divisible_5():
    do_test_num_divisible(lb=1, ub=25, p=27, q=5, expected=5)


def test_num_divisible_6():
    do_test_num_divisible(lb=1, ub=25, p=27, q=29, expected=0)