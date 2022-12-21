def select_row_col(x, row_idx=None, col_idx=None):
    """
    Select a subset of rows or columns in the two-dimensional array x. 
    Inputs:
        x: input two-dimensional array 
        row_idx: a list of row index we are selecting, None if not specified
        col_idx: a list of column index we are selecting, None if not specified
    Returns: a two-dimensional array where we have selected based on the 
        specified row_idx and col_idx
    """

    # YOUR CODE HERE
    # Replace None with an appropriate return value
    return None


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
import numpy as np
sys.path.append('../')

import test_utils as utils

def test_select_row_col():
    x = np.arange(20).reshape(4, 5)

    def custom_get_cols(x, cols):
        out = np.stack([x[:, r] for r in cols], -1)
        return out
    
    def custom_get_rows(x, rows):
        out = np.stack([x[r] for r in rows])
        return out
    
    def custom_get_rows_cols(x, rows, cols):
        row_out = np.stack([x[r] for r in rows])
        out = np.stack([row_out[:, r] for r in cols], -1)
        return out
    
        
    for tgt_cols in [[0], [1, 2, 3], [3, 2, 1], [2, 1, 3, 4, 0]]:

        recreate_msg = utils.gen_recreate_msg('select_row_col', x, None, tgt_cols)
        
        result = select_row_col(x, None, tgt_cols)
    
        utils.check_none(result, recreate_msg)
        utils.check_is_ndarray(result, recreate_msg)

        expected_shape = (4, len(tgt_cols))
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        expected_value = custom_get_cols(x, tgt_cols)

        utils.check_array_equal(result, expected_value, 
                          recreate_msg)
        
    for tgt_rows in [[0], [1, 2, 3], [3, 2, 1], [2, 1, 3, 0]]:

        recreate_msg = utils.gen_recreate_msg('select_row_col', x, tgt_rows, None)
        
        result = select_row_col(x, tgt_rows, None)
    
        utils.check_none(result, recreate_msg)
        utils.check_is_ndarray(result, recreate_msg)

        expected_shape = (len(tgt_rows), 5)
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        expected_value = custom_get_rows(x, tgt_rows)

        utils.check_array_equal(result, expected_value, 
                          recreate_msg)
    
    for tgt_rows, tgt_cols in [([0],[0]), ([1, 2, 3],[1, 3]), ([3, 1],[0,2])]:

        recreate_msg = utils.gen_recreate_msg('select_row_col', x, tgt_rows, tgt_cols)
        
        result = select_row_col(x, tgt_rows, tgt_cols)
    
        utils.check_none(result, recreate_msg)
        utils.check_is_ndarray(result, recreate_msg)

        expected_shape = (len(tgt_rows), len(tgt_cols))
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        expected_value = custom_get_rows_cols(x, tgt_rows, tgt_cols)

        utils.check_array_equal(result, expected_value, 
                          recreate_msg)
    
    for tgt_rows, tgt_cols in [(None, None)]:

        recreate_msg = utils.gen_recreate_msg('select_row_col', x, None, None)
        
        result = select_row_col(x, None, None)
    
        utils.check_none(result, recreate_msg)
        utils.check_is_ndarray(result, recreate_msg)

        expected_shape = (x.shape[0], x.shape[1])
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        utils.check_array_equal(result, x, recreate_msg)
