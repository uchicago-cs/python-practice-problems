def add_one_and_multiply(a, x):
    """ Add 1 to a, and multiply by x"""

    ### YOUR CODE GOES HERE
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

def do_test_add_one_and_multiply(a, x, expected):
    recreate_msg = utils.gen_recreate_msg("add_one_and_multiply", *(a, x))

    actual = add_one_and_multiply(a, x)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_add_one_and_multiply_1():
    do_test_add_one_and_multiply(a=0, x=0, expected=0)


def test_add_one_and_multiply_2():
    do_test_add_one_and_multiply(a=5, x=2, expected=12)


def test_add_one_and_multiply_3():
    do_test_add_one_and_multiply(a=5, x=0, expected=0)


def test_add_one_and_multiply_4():
    do_test_add_one_and_multiply(a=9, x=1, expected=10)


def test_add_one_and_multiply_5():
    do_test_add_one_and_multiply(a=9, x=-2, expected=-20)


def test_add_one_and_multiply_6():
    do_test_add_one_and_multiply(a=-11, x=2, expected=-20)