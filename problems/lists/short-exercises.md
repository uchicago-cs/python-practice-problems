# Short Exercises: Lists

### Exercise #1

**File**: [count_greater_than_val.py](count_greater_than_val.py)

Given a list of integers ``lst`` and a variable ``val``, write a loop to count the number of values in the list that are strictly greater than ``val``. For example, given the list ``[-1, -2, -3, -4]`` and ``0`` for ``val``, the result would be zero because there are no values that are strictly greater than zero in the list.

### Exercise #2

**File**: [negate_list.py](negate_list.py)

Given a list of integers ``lst``, create a *new* list with its values negated. For example, given list ``[-1, 2, -3, 4]``, the result should be this *new* list: ``[1, -2, 3, -4]``

### Exercise #3

**File**: [has_more.py](has_more.py)

Complete the function ``has_more``, which takes two lists and a target value and returns ``True`` if the first list has more of the target value than the second list, and ``False`` otherwise. For example, given the lists ``[1, 1, 2, 3]`` and ``[2, 1, 1, 1]``, and target ``1``, the function would return ``False``. There are not more 1s in the first list than than the second. This is a good place to use a helper function to count the number of occurrences of a target value in a list. You **may not** use the built-in ``count`` method.

### Exercise #4

**File**: [make_star_strings.py](make_star_strings.py)

Complete the function ``make_star_strings``, which takes a list of nonnegative integers and returns a list of strings where each string is a string of stars (``*``). The number of stars in each string is the corresponding number in the input list. For example, a call to ``make_star_strings`` with the list ``[2, 1, 3, 0]`` would return ``["**", "*", "***", ""]``. Notice that a zero in the input list produces the empty string (a string with zero stars).

### Exercise #5

**File**: [replace.py](replace.py)

Complete the function ``replace``, which takes a list, a value ``replacee``, and another value ``replacer``, and replaces all instances of ``replacee`` with ``replacer`` in the list *in place*. For example, if the input variable ``lst`` has the values ``[2, 1, 4, 1]``, calling ``replace(lst, 1, 3)`` will update the value of ``lst`` to be ``[2, 3, 4, 3]``.

### Exercise #6

**File**: [rows_and_columns_contain.py](rows_and_columns.py)

Complete the function ``rows_and_columns_contain``, which takes a list of lists and a target value, and returns ``True`` if the target value occurs at least once in every row and column of the input, and ``False`` otherwise. Here are some sample uses of the function and expected results:

```python
grid =  [[2, 1, 1, 2],
         [1, 2, 3, 1],
         [3, 3, 1, 2],
         [1, 2, 1, 3]]

rows_and_columns_contain(grid, 1) # expected result: True

rows_and_columns_contain(grid, 2) # expected result: False (no 2 in third column)

rows_and_columns_contain(grid, 3) # expected result: False (no 3 in first row)
```

You can assume that the input list has at least one row, but you should not assume that the number of rows and the number of columns are the same.
