# Short Exercises: Numpy

## Arrays

### Exercise #1

**File**: [compute_matching.py](compute_matching.py)

Complete the function ``compute_matching``, which takes two lists of equal length and returns a list of the same length where the ith element is ``True`` if the ith elements of the two lists are equal.  For example, given the arrays ``np.array([10, 20, 30])`` and ``np.array([10, 30, 30])``, the function would return ``np.array([True, False, True])``.

### Exercise #2

**File**: [compute_matching_indices.py](compute_matching_indices.py)

Complete the function ``compute_matching_indices``, which takes two arrays of equal length and returns an array of the indices where the elements of the two arrays are equal. For example, given the arrays ``np.array([10, 20, 30])`` and ``np.array([10, 30, 30])``, the function would return ``np.array([0, 2])``.

## Arrays and scalars

### Exercise #1

**File**: [powers.py](powers.py)

Complete the function ``powers(N, p)``, which computes the first ``N`` powers of ``p``. For example, ``powers(5,2)`` would return the array ``np.array([1, 2, 4, 8, 16])``.

## Masking array values

### Exercise #1

**File**: [clip_values.py](clip_values.py)

Complete the function ``clip_values``, which takes in an n-dimensional array and returns a **new array** with its values clipped between ``min_val`` and ``max_val``. For example, ``clip_values(np.array([1, 2, 3]), min_val=2)`` would return ``np.array([2, 2, 3]`` and ``clip_values(np.array([1, 2, 3]), max_val=2)`` would return ``np.array([1, 2, 2]``. Remember to return a **new** array and to not modify the input array.

## Indexing

### Exercise #1

**File**: [find_closest_value.py](find_closest_value.py)

Complete the function ``find_closest_value`` which will find the entry and the value in an one-dimensional array that is closest to the mean of the array. For example ``find_closest_value(np.array([1.0, 2.0, 3.0]))`` would return  ``(1, 2.0)`` and ``find_closest_value(np.array([5.0, 1.0, 8.0]))`` would return ``(0, 5.0)``.

### Exercise #2

**File**: [select_row_col.py](select_row_col.py)

Complete the function ``select_row_col(x, row_idx, col_idx)`` that takes in a 2-dimensional array ``x`` and returns a subset of rows or columns or sub-array specified by ``row_idx`` and ``col_idx``. If you specify ``row_idx`` as a list and ``col_idx`` as None, you will return a subset of rows. Similarly, if you specify ``row_idx`` as None and ``col_idx`` as a list, you will return a subset of columns. If you specify ``row_idx`` as a list and ``col_idx`` as a list, you will return a sub-array specified by the given rows and columns. If you specify both ``row_idx`` and ``col_idx`` as None, you will return the array itself. For example, 

```python
In [1]: x = np.array([[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]])

In [2]: se5.select_row_col(x, [1, 2], None)
Out[2]:
array([[3, 4, 5],
       [6, 7, 8]])

In [3]: se5.select_row_col(x, None, [1, 2])
Out[3]:
array([[1, 2],
       [4, 5],
       [7, 8]])

In [4]: se5.select_row_col(x, [1, 2], [0, 2])
Out[4]:
array([[3, 5],
       [6, 8]])
```
