def count_greater_than_val(lst, val):
    """
    Count the number of numbers in the list that are strictly greater than the value of val.
    """

    ### EXERCISE 5 -- YOUR CODE GOES HERE
    # Replace the following line with your code.
    # After running your code, variable n should contain the value
    # we ask you to compute in this exercise.
    n = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return n


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_count_greater_than_val(lst, val, expected):
    recreate_msg = utils.gen_recreate_msg("count_greater_than_val", *(lst, val))

    actual = count_greater_than_val(lst, val)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_count_greater_than_val_1():
    do_test_count_greater_than_val(lst=[1, 2, 3, 4], val=0, expected=4)


def test_count_greater_than_val_2():
    do_test_count_greater_than_val(lst=[-1, -2, -3, -4], val=0, expected=0)


def test_count_greater_than_val_3():
    do_test_count_greater_than_val(lst=[-1, 2, -3, 4], val=0, expected=2)


def test_count_greater_than_val_4():
    do_test_count_greater_than_val(lst=[1, 10, 11, 2, 12, 13], val=10, expected=3)


def test_count_greater_than_val_5():
    do_test_count_greater_than_val(lst=[], val=10, expected=0)
    