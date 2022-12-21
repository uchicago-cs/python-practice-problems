def has_more(lst1, lst2, target):
    """
    Determine which list contains more of the target value
    Inputs:
      lst1 (list): first list
      lst2 (list): second list
      target: the target value
    Returns: True if lst1 contains more of target, False otherwise
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


def do_test_has_more(lst1, lst2, target, expected):
    recreate_msg = utils.gen_recreate_msg("has_more", *(lst1, lst2, target))

    actual = has_more(lst1, lst2, target)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_has_more_1():
    lst1 = []
    lst2 = []
    do_test_has_more(lst1=lst1, lst2=lst2, target=1, expected=False)

def test_has_more_2():
    lst1 = []
    lst2 = [1]
    do_test_has_more(lst1=lst1, lst2=lst2, target=1, expected=False)

def test_has_more_3():
    lst1 = [1]
    lst2 = [1]
    do_test_has_more(lst1=lst1, lst2=lst2, target=1, expected=False)

def test_has_more_4():
    lst1 = [1]
    lst2 = []
    do_test_has_more(lst1=lst1, lst2=lst2, target=1, expected=True)

def test_has_more_5():
    lst1 = [1, 2, 1]
    lst2 = [1, 2, 2]
    do_test_has_more(lst1=lst1, lst2=lst2, target=1, expected=True)

def test_has_more_6():
    lst1 = [1, 2, 2]
    lst2 = [2, 1, 1]
    do_test_has_more(lst1=lst1, lst2=lst2, target=1, expected=False)

def test_has_more_7():
    lst1 = [1, 2, 2, 1]
    lst2 = [2, 1, 1]
    do_test_has_more(lst1=lst1, lst2=lst2, target=1, expected=False)

def test_has_more_8():
    lst1 = [1, 1, 2, 2]
    lst2 = [2, 1, 1, 1, 1]
    do_test_has_more(lst1=lst1, lst2=lst2, target=2, expected=True)