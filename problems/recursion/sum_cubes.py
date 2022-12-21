def sum_cubes(n):
    """
    Recursively calculates the sum of the first n positive cubes.
    Input:
        n: positive integer.
    
    Returns: (integer) the value of the sum 1^3 + 2^3 + ... + n^3.
    
    This function may not use any loops or list comprehensions.
    """

    pass


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_sum_cubes(n):
    recreate_msg = utils.gen_recreate_msg('sum_cubes', n)
    actual = sum_cubes(n)
    expected = sum(n ** 3 for n in range(n + 1))
    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_sum_cubes_1():
    do_test_sum_cubes(1)

def test_sum_cubes_2():
    do_test_sum_cubes(2)

def test_sum_cubes_3():
    do_test_sum_cubes(3)

def test_sum_cubes_4():
    do_test_sum_cubes(4)

def test_sum_cubes_5():
    do_test_sum_cubes(5)

def test_sum_cubes_6():
    do_test_sum_cubes(6)

def test_sum_cubes_7():
    do_test_sum_cubes(7)

def test_sum_cubes_8():
    do_test_sum_cubes(8)

def test_sum_cubes_9():
    do_test_sum_cubes(9)

def test_sum_cubes_10():
    do_test_sum_cubes(10)

def test_sum_cubes_11():
    do_test_sum_cubes(15)

def test_sum_cubes_12():
    do_test_sum_cubes(19)

def test_sum_cubes_13():
    do_test_sum_cubes(24)

def test_sum_cubes_14():
    do_test_sum_cubes(30)

def test_sum_cubes_15():
    do_test_sum_cubes(31)

def test_sum_cubes_16():
    do_test_sum_cubes(36)

def test_sum_cubes_17():
    do_test_sum_cubes(42)

def test_sum_cubes_18():
    do_test_sum_cubes(50)

def test_sum_cubes_19():
    do_test_sum_cubes(81)

def test_sum_cubes_20():
    do_test_sum_cubes(100)