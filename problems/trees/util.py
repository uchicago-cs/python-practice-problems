import json
from tree import Tree


def load_trees(filename):
    """
    Loads trees from a json file. The json file
    should consist of a dictionary mapping tree
    names to trees represented as lists.
    Input:
        filename: (string) name of the json file.
    Returns: dictionary mapping tree names (strings)
        to Tree instances.
    """

    with open(filename) as f:
        trees_json = json.load(f)
    return {name: list_to_tree(lst) for name, lst in trees_json.items()}


def list_to_tree(lst):
    """
    Converts a list to a tree. The first element
    of the list should be a dictionary mapping
    attributes to values. The remaining elements
    of the list are the child subtrees, in the
    same format.
    Input:
        lst: list representing a tree.
    
    Returns: a Tree instance.
    """

    root = lst[0]
    children = lst[1:]
    t = Tree(root.get('key'), root.get('value'))
    for attrname, attrvalue in root.items():
        if attrname not in ['key', 'value']:
            setattr(t, attrname, attrvalue)
    for child_list in children:
        t.add_child(list_to_tree(child_list))
    return t