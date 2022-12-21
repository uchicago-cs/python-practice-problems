def make_star_strings(lst):
    """
    Create a list of star strings
    Input:
      lst (list of nonnegative integers): the list
    Returns: A list of strings of stars (*)
    """

    ### Replace pass with your code
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


def do_test_make_star_strings(lst, expected):
    recreate_msg = utils.gen_recreate_msg("make_star_strings", *(lst,))

    actual = make_star_strings(lst)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_make_star_strings_1():
    lst = []
    do_test_make_star_strings(lst=lst, expected=[])


def test_make_star_strings_2():
    lst = [1]
    do_test_make_star_strings(lst=lst, expected=["*"])


def test_make_star_strings_3():
    lst = [3]
    do_test_make_star_strings(lst=lst, expected=["***"])


def test_make_star_strings_4():
    lst = [1, 2, 3]
    do_test_make_star_strings(lst=lst, expected=["*", "**", "***"])


def test_make_star_strings_5():
    lst = [1, 2, 3, 2, 0]
    do_test_make_star_strings(lst=lst, expected=["*", "**", "***", "**", ""])


def test_make_star_strings_6():
    lst = [2, 1, 5, 3, 3]
    do_test_make_star_strings(lst=lst, expected=["**", "*", "*****", "***", "***"])