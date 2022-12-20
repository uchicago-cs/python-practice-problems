# Short Exercises: Programming Basics


## Expressions and Control Flow

In these exercises, you will be asked to write an expression or a simple control flow statement.
**You should start by informally testing your code in the Python interpreter**. Once you're comfortable with your
solution, you can enter it into the provided file so you can run automated tests on it.


### Exercise #1

**File**: [add_one_and_multiply.py](add_one_and_multiply.py)

Given two integer variables, `a` and `x`, write a *single* expression that adds `1` to `a`, and then multiplies the resulting value by `x`


### Exercise #2

**File**: [out_of_range.py](out_of_range.py)

Given three integer variables, `x`, `lb`, and `ub`, write a *single* boolean expression that evaluates to `True`  if `x` is outside the range between `lb` and `ub` (inclusive), and `False` otherwise.  For example, if `x` is `11`, `lb` is `1` and `ub` is `10`, then `x` is outside the range from `lb` to `ub` and the result would be `True`.  If, on the other hand, `x` is `10`, `lb` is `1` and `ub` is `10` then `x` is not outside the range from `lb` to `ub` inclusive and the result would be `False`.

### Exercise #3

**File**: [number_string.py](number_string.py)

Given an integer variable `x`, write a conditional statement that will assign to a variable `s` the string value `"POSITIVE"`, `"NEGATIVE"`, or `"ZERO"` (depending on whether `x` is positive, negative, or zero, respectively)

### Exercise #4

**File**: [num_divisible.py](num_divisible.py)

Given integer variables `lb`, `ub`, `p`, and `q`, write a loop that will count how many numbers between `lb` and `ub` (inclusive) are divisible by `p` or divisible by `q`, but not divisible by both `p` and `q`. For example, suppose `p` is `2` and `q` is `3`. If we counted how many numbers between 1 and 20 were divisible by either 2 or 3 (but not both), the result would be 10 (because seven values--2, 4, 8, 10, 14, 16, 20--are divisible by `2` but not `3` and three values--3, 9, and 15--are divisible by `3` and not by `2` for a total of 10 values.

## Functions

In these exercises, you will be asked to complete or implement a function in the provided file.

### Exercise #1

**File**: [peep.py](peep.py)

Complete the function `peep`, which takes two digits `p` and `e`,  returns `True` if the digits `p` and `e` can replace $p$ and $e$ so that $peep$ is equal to $(pp)^e$, and `False` otherwise. For example, the call `peep(1, 3)` should return `True` since $1331 = (11)^3$. You can assume that the inputs `p` and `e` are digits (the numbers 0-9).
