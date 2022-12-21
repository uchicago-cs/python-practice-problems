# Short Exercises: Recursion

## Recursion with numbers and lists

### Exercise #1

**File**: [sum_cubes.py](sum_cubes.py)

Complete the function ``sum_cubes``, which takes an integer :math:`n` and computes the sum
$$1^3 + 2^3 + 3^3 + \dots + n^3.$$

Do not use loops nor list comprehensions.

### Exercise #2

**File**: [sublists.py](sublists.py)

A *sublist* of a list ``lst`` is a list that contains some (possibly all or none) of the elements of `lst`, in the same order. For example, the following are all the sublists of ``['A', 'B', 'C']``:

```python
[]                  ['A']
['C']               ['A', 'C']
['B']               ['A', 'B']
['B', 'C']          ['A', 'B', 'C']
```

You will complete the function ``sublists``, which takes a list of values and returns a list of all sublists of the input.

To figure out how to solve the sublists problem recursively, focus on the example above, which shows the solution to the sublists problem on the input ``['A', 'B', 'C']``. Identify how the first column above is the solution to the sublists problem on a simpler input. Then, find a relationship between the first column and the second column.
