from tree import Tree

def prune_tree(tree, keys_to_discard):
    '''
    Returns a new tree with that is identical to the original tree, except
    that any node whose key is in keys_to_discard is removed, along with its
    descendants. If the key of the root is in keys_to_discard, then
    <replace this with a description of how your code behaves in this case>

    Inputs:
        tree: a Tree instance.
        keys_to_discard: set of keys.
    
    Returns: (Tree) the pruned tree.
    '''
    
    pass


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
import pytest
import util
sys.path.append('../')

import test_utils as utils
import tree_test_utils as tree_utils

def do_test_prune_tree(trees_original_expected, tree_name, keys_to_prune):
    trees, original_trees, expected_trees = trees_original_expected
    recreate_msg = tree_utils.gen_recreate_msg_with_trees('prune_tree', 
                                                    tree_name, keys_to_prune)
    actual = prune_tree(trees[tree_name], keys_to_prune)
    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected_trees[tree_name], recreate_msg)
    tree_utils.check_tree_equals(actual, expected_trees[tree_name], recreate_msg)
    tree_utils.check_tree_unmodified(trees[tree_name], original_trees[tree_name], 
                                     recreate_msg)


def test_prune_tree_1(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_1", {'D', 'B'})

def test_prune_tree_2(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_2", {'C', 'E'})

def test_prune_tree_3(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_3", {'E'})

def test_prune_tree_4(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_4", {'b', 'I', 'J', 'c', 'M'})

def test_prune_tree_5(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_5", {'Q', 'G', 'C'})

def test_prune_tree_6(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_6", {'V2'})

def test_prune_tree_7(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_7", {'V9'})

def test_prune_tree_8(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_8", set())

def test_prune_tree_9(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_9", {'V9', 'V8'})

def test_prune_tree_10(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_10", 
        {'V11', 'V8', 'V7', 'V4', 'V5'})

def test_prune_tree_11(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_11", {'V80', 'V90'})

def test_prune_tree_12(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_12", 
        {'V26', 'V9', 'V1', 'V6', 'V27'})

def test_prune_tree_13(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_13", {'V0', 'V1', 'V4', 'V3'})

def test_prune_tree_14(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_14", 
        {'V2', 'V0', 'V1', 'V7', 'V4', 'V6', 'V3', 'V5'})

def test_prune_tree_15(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_15", 
        {'V2', 'V48', 'V49', 'V46', 'V45', 'V47'})

def test_prune_tree_16(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_16", {'V10', 'V20', 'V30'})

def test_prune_tree_17(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_17", {'V3', 'V7'})

def test_prune_tree_18(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_18", 
        {'V26', 'V27', 'V24', 'V21', 'V28', 'V25', 'V23', 'V22'})

def test_prune_tree_19(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_19", {'V18'})

def test_prune_tree_20(trees_prune_tree):
    do_test_prune_tree(trees_prune_tree, "tree_20", 
        {'V12', 'V42', 'V46', 'V7', 'V30', 'V29', 'V60', 'V17', 'V36'})

@pytest.fixture(scope="session")
def trees_prune_tree():
    """
    Fixture for loading the trees for prune_tree
    """
    trees, original_trees = get_trees()
    expected_trees = util.load_trees("sample_trees_pruned.json")
    return trees, original_trees, expected_trees

def get_trees():
    trees = util.load_trees("sample_trees.json")
    original_trees = util.load_trees("sample_trees.json")
    return trees, original_trees