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