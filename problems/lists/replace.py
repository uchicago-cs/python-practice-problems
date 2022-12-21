def replace(lst, replacee, replacer):
    """
    Replace one element in a list with another
    Input:
      lst (list): the list
      replacee: the element to replace
      replacer: the element to replace replacee with
    Returns: None, modifies lst in-place
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


def do_test_replace(lst, replacee, replacer, expected):
    recreate_msg = utils.gen_recreate_msg("replace", *(lst, replacee, replacer))

    lst_copy = lst[:]
    actual = replace(lst_copy, replacee, replacer)

    utils.check_expected_none(actual, recreate_msg)
    utils.check_equals(lst_copy, expected, recreate_msg)


def test_replace_1():
    do_test_replace(lst=[], replacee=1, replacer=2, expected=[])


def test_replace_2():
    do_test_replace(lst=[1], replacee=1, replacer=2, expected=[2])


def test_replace_3():
    do_test_replace(lst=[3], replacee=1, replacer=2, expected=[3])


def test_replace_4():
    do_test_replace(lst=[1, 2, 3, 4], replacee=1, replacer=2, expected=[2, 2, 3, 4])


def test_replace_5():
    do_test_replace(lst=[1, 2, 3, 4], replacee=4, replacer=3, expected=[1, 2, 3, 3])


def test_replace_6():
    do_test_replace(lst=[3, 2, 3, 2], replacee=2, replacer=1, expected=[3, 1, 3, 1])


def test_replace_7():
    do_test_replace(lst=[2, 2, 2, 2], replacee=2, replacer=1, expected=[1, 1, 1, 1])


def test_replace_8():
    do_test_replace(lst=[2, 2, 2, 2, 2], replacee=3, replacer=1, expected=[2, 2, 2, 2, 2])