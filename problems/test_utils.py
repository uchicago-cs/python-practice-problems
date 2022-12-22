def gen_recreate_msg(function, *params):
    params_str = ", ".join([str(p) for p in params])

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += f"  {function}({params_str})"

    return recreate_msg


def check_none(actual, recreate_msg=None):
    msg = "The function returned None."
    msg += " Did you forget to replace the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg

def check_expected_none(actual, recreate_msg=None):
    msg = "The function is expected to return None."
    msg += f" Your function returns: {actual}"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is None, msg


def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The function returned a value of the wrong type.\n"
    msg += f"  Expected return type: {expected_type.__name__}.\n"
    msg += f"  Actual return type: {actual_type.__name__}."
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg


def check_equals(actual, expected, recreate_msg=None):
    msg = f"Actual ({actual}) and expected ({expected}) values do not match."
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg


def check_list_unmodified(param_name, before, after, recreate_msg=None):
    msg = f"You modified the contents of {param_name} (this is not allowed).\n"
    msg += f"  Value before your code: {before}\n"
    msg += f"  Value after your code:  {after}"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert before == after, msg


# Utils ported over from the NumPy problems
import numpy as np

def check_is_ndarray(actual, recreate_msg=None):
    check_type(actual, np.zeros(1), recreate_msg)

def check_dtype(array, expected, recreate_msg=None):
    actual_dtype = array.dtype
    expected_dtype = expected

    msg = "The function returned an array of the wrong dtype.\n"
    msg += "  Expected return dtype: {}.\n".format(expected_dtype)
    msg += "  Actual return dtype: {}.".format(actual_dtype)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual_dtype == expected_dtype, msg

def check_array_equal(actual, expected, recreate_msg):
    msg = "The function returned the wrong array"
    msg += " Expected array: {}\n".format(expected)
    msg += " Actual returned array: {}\n".format(actual)

    if recreate_msg is not None:
        msg += "\n" + recreate_msg
    
    np.testing.assert_allclose(actual, expected, err_msg = msg, verbose=False)


# Utils ported over for recursion problems
def check_parameter_unmodified(actual, expected, param, recreate_msg=None):
    msg = ("Parameter {} has been modified:\n"
        "Actual ({}) and original ({}) values of {}" 
        "do not match.").format(param, param, actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg


# Utils ported over for tree problems
from tree import Tree

def pretty_print_repr(x):
    return repr(x)

def check_tree_equals(t, expected_t, recreate_msg):
    check_tree_helper(t, expected_t, 
        "Actual and expected values do not match:", recreate_msg)

def gen_recreate_msg_with_trees(function, tree_name, *params):
    params_str = "".join([", " + pretty_print_repr(p) for p in params])
    lines = ['import util',
             'trees = util.load_trees("sample_trees.json")',
             '{}(trees["{}"]{})'.format(
                function, tree_name, params_str)]
    return gen_recreate_msg_by_lines(lines)

def gen_recreate_msg_by_lines(lines):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  " + "\n  ".join(lines)
    return recreate_msg

def check_tree_unmodified(t, expected_t, recreate_msg):
    check_tree_helper(t, expected_t, "Tree has been modified:", recreate_msg)

def check_tree_helper(t, expected_t, top_msg, recreate_msg):
    expected_attributes = vars(expected_t)

    node_error_prefix = "Checking a node with " + ", ".join(
        ["{}={}".format(attr, repr(getattr(t, attr, "[not assigned]")))
        for attr in expected_attributes if attr != 'children']) + \
        "\n{}\n".format(top_msg)

    for attr in expected_attributes:
        assert hasattr(t, attr), \
            node_error_prefix + \
            "Node is missing attribute {}.\n".format(attr) + \
            recreate_msg

        if attr != 'children':
            assert getattr(t, attr) == getattr(expected_t, attr), \
            node_error_prefix + ("Node has incorrect {}. "
                "Got {}, expected {}.\n").format(attr,
                repr(getattr(t, attr)), repr(getattr(expected_t, attr))) + \
                recreate_msg
    
    expected_attributes_set = set(expected_attributes.keys())
    actual_attributes_set = set(vars(t).keys())
    assert actual_attributes_set == expected_attributes_set, \
            node_error_prefix + \
            "Node has extra attributes {}.\n".format(
                ", ".join(actual_attributes_set - expected_attributes_set)) + \
            recreate_msg


    children = list(t.children)
    expected_children = list(expected_t.children)

    if expected_children == []:
        assert children == [], node_error_prefix + \
            "Expected node to have no children, but it has children.\n" + \
            recreate_msg
    else:
        for c in children:
            assert isinstance(c, Tree), node_error_prefix + \
                "Node has a child that is not a Tree: {}\n".format(c) + \
                recreate_msg

        # This assumes no node has two children with the same key
        sorted_children = sorted(children, key=lambda st: st.key)
        sorted_expected_children = sorted(
            expected_children, key=lambda st: st.key)
        keys = [c.key for c in sorted_children]
        expected_keys = [c.key for c in sorted_expected_children]


        assert keys == expected_keys, node_error_prefix + \
            "Expected node to have children with keys {} " \
            "but the children's keys are {}.\n".format(expected_keys, keys) + \
            recreate_msg

        for child, expected_child in zip(sorted_children,
                                         sorted_expected_children):
            check_tree_helper(child, expected_child, top_msg, recreate_msg)