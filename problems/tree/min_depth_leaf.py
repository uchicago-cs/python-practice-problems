def min_depth_leaf(tree):
    """
    Computes the minimum depth of a leaf in the tree (length of shortest
    path from the root to a leaf).
    Input:
        tree: a Tree instance.
    
    Returns: (integer) the minimum depth of of a leaf in the tree.
    """

    pass


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
from tree import Tree
import pytest
import util
sys.path.append('../')

import test_utils as utils

def do_test_min_depth_leaf(trees_and_original_trees, tree_name, expected):
    trees, original_trees = trees_and_original_trees
    recreate_msg = utils.gen_recreate_msg_with_trees('min_depth_leaf', tree_name)
    actual = min_depth_leaf(trees[tree_name])
    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)
    utils.check_tree_unmodified(trees[tree_name], original_trees[tree_name], 
                                recreate_msg)


def test_min_depth_leaf_1(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_1", 1)

def test_min_depth_leaf_2(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_2", 1)

def test_min_depth_leaf_3(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_3", 5)

def test_min_depth_leaf_4(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_4", 4)

def test_min_depth_leaf_5(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_5", 3)

def test_min_depth_leaf_6(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_6", 2)

def test_min_depth_leaf_7(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_7", 2)

def test_min_depth_leaf_8(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_8", 2)

def test_min_depth_leaf_9(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_9", 49)

def test_min_depth_leaf_10(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_10", 2)

def test_min_depth_leaf_11(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_11", 6)

def test_min_depth_leaf_12(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_12", 2)

def test_min_depth_leaf_13(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_13", 4)

def test_min_depth_leaf_14(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_14", 4)

def test_min_depth_leaf_15(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_15", 3)

def test_min_depth_leaf_16(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_16", 4)

def test_min_depth_leaf_17(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_17", 2)

def test_min_depth_leaf_18(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_18", 6)

def test_min_depth_leaf_19(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_19", 3)

def test_min_depth_leaf_20(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_20", 2)

@pytest.fixture(scope="session")
def trees_min_depth_leaf():
    """
    Fixture for loading the trees for min_depth_leaf
    """
    return get_trees()

def get_trees():
    trees = util.load_trees("sample_trees.json")
    original_trees = util.load_trees("sample_trees.json")
    return trees, original_trees