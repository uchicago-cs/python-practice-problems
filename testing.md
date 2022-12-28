# How to Test your Solutions

All the practice problems provide some mechanism to test your solution,
depending on the problem type:

- [Be-a-Computer Problems](#be-a-computer-problems)
- [Short Exercises](#short-exercises)
- [Advent of Code](#advent-of-code)

## Be-a-Computer Problems

For the Be-a-Computer problems, you can simply copy-paste the code into
the IPython interpreter to run it and observe the result of the code.
Make sure you try to work through the problem first before doing this!

## Short Exercises

Once you've written a piece of code, you will want to test that it
works as expected. There are broadly two ways of doing this:

- **Manual testing**: This just involves running the code you wrote with
  some sample values, to check whether it behaves as expected.
  For example, if you were writing an expression to compute whether
  a year is a leap year, you may try running your code in IPython with a few
  leap years and a few non-leap years, to see whether your code
  correctly identifies the leap years.
- **Automated testing**: There are automated testing frameworks that allow
  you to specify a series of tests you want to run on your code,
  and which make it easy to automatically re-run all those tests. For example,
  following the leap year example, you wouldn't have to manually test
  each year value one by one; instead, the testing framework would test
  all these year values for you, and would report back how many produced the
  expected result.

All the short exercises in this repository include a suite of automated
tests that you can use to check whether your code is working correctly,

Because the automated tests are easy to run , you may be tempted to do the
following: write some code, immediately try running the automated
tests to find a test that fails, make a guess as to how to modify your code,
and then repeat the process until all of the tests pass.

This is not a good way to test your code.
Instead, you should start by doing some manual testing
to get a sense of whether it is working before
you try the automated tests. In this page, we
describe how to do this.

### Manual testing


Let's say you're working on the Programming Basics [Short Exercises](problems/basics/short-exercises.md)
and, specifically,
on the `add_one_and_multiply` exercise. You can start by
informally testing your expression on IPython. For example,
you could do this:

    In [1]: a = 5

    In [2]: x = 2

    In [3]: a + 1 * x
    Out[3]: 7

That doesn't seem quite right: the result should've been 12
(if we add 1 to 5, that gives us 6, which multiplied by 2
gives us 12). Looks like you need to experiment a bit
more in IPython!

Let's say you've figured out what you believe it the correct
expression, and you've added the code to the `add_one_and_multiply.py` file.
You should then try making some sample calls to the `add_one_and_multiply`
function:

    In [1]: %load_ext autoreload

    In [2]: %autoreload 2

    In [3]: from add_one_and_multiply import add_one_and_multiply

    In [4]: add_one_and_multiply(5, 2)
    Out[4]: 12

    In [5]: add_one_and_multiply(7, 0)
    Out[5]: 0

If you get the wrong answer for some sample input, stop to reason why
your code is behaving the way it is and think about how to modify it
to get the correct result.

In short exercises like the one above, it is sometimes enough to look
at the code and figure our why it is not working. However, for more
complex code, you will want to follow a more rigorous approach. 
You should make a hypothesis about what might be
wrong and use `print` statements to print out key values to help you
verify or disprove your hypothesis. You can also find a lot of tips
on how to debug your code in [The Debugging Guide](https://uchicago-cs.github.io/debugging-guide/)

After you've done some manual testing, and get the sense that your function
seems to be working for, at least, a few simple inputs, you should
try running the automated tests. The tests could reveal that there are
still issues with your function and, at that point, you could repeat
the same process we described above. The important thing is that
you always have an idea in your head about how your code works,
and don't make random changes that you don't fully understand.

### Automated testing

Now on to the automated tests. We use the [https://pytest.org/](pytest)
Python testing framework to provide automated tests in the short exercises.

If you are a UChicago student, pytest is available on the CS machines. 
To run our automated tests, you will use the
`pytest` command from the **Linux command line** (not from within
`ipython3`).  We recommend opening a new terminal window for running
this command, which will allow you to go back and forth easily between
testing code by hand in `ipython3` in one terminal window and running the test suite using
`pytest` in the other. 

Each of the files we provide for the short exercises includes a series
of pytest tests which can be run like this:

    pytest <exercise file>

For example, to run all the tests for `add_one_and_multiply`, you can run 
the following command from the **Linux command-line**:

.. code-block:: bash

    $ pytest add_one_and_multiply.py

(Recall that the `$` represents the
prompt and is not included in the command.)

You may also want to run the tests as follows:

.. code-block:: bash

    $ pytest -v -x add_one_and_multiply.py

This is what each of the flags does:

  - The flag `-v` means run in verbose mode; this gives us a more detailed readout of the test results.

  - The flag `-x` means that pytest should stop running tests after a single test failure. Omitting the `-x` 
    option makes sense when you want to get a sense of which tests are passing and which ones aren't; 
    however, when debugging your code, you should always use the `-x` option so that you can focus 
    on one error at a time.


Here is (slightly-abridged) output from using this command to test a
correct implementation of `add_one_and_multiply`:

    $ py.test -v -x add_one_and_multiply.py
    ================================= test session starts ==================================
    platform linux -- Python 3.8.10, pytest-6.2.1, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3
    collected 6 items                                                                      

    add_one_and_multiply.py::test_add_one_and_multiply_1 PASSED                      [ 16%]
    add_one_and_multiply.py::test_add_one_and_multiply_2 PASSED                      [ 33%]
    add_one_and_multiply.py::test_add_one_and_multiply_3 PASSED                      [ 50%]
    add_one_and_multiply.py::test_add_one_and_multiply_4 PASSED                      [ 66%]
    add_one_and_multiply.py::test_add_one_and_multiply_5 PASSED                      [ 83%]
    add_one_and_multiply.py::test_add_one_and_multiply_6 PASSED                      [100%]

    ================================== 6 passed in 0.10s ===================================

This output shows that our code passed all six tests
for `add_one_and_multiply`.  

If you fail a test, pytest will print out some information about what went wrong. For example,
let's say you specified the following expression, which we saw earlier was incorrect::

    a + 1 * x

This would pass the first test, but would fail the second one:

    $ py.test -v -x add_one_and_multiply.py
    ================================= test session starts ==================================
    platform linux -- Python 3.8.10, pytest-6.2.1, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3
    collected 6 items                                                                      

    add_one_and_multiply.py::test_add_one_and_multiply_1 PASSED                      [ 16%]
    add_one_and_multiply.py::test_add_one_and_multiply_2 FAILED                      [ 33%]

    ======================================= FAILURES =======================================
    _____________________________ test_add_one_and_multiply_2 ______________________________

        def test_add_one_and_multiply_2():
    >       do_test_add_one_and_multiply(a=5, x=2, expected=12)

    add_one_and_multiply.py:39: 
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    add_one_and_multiply.py:31: in do_test_add_one_and_multiply
        utils.check_equals(actual, expected, recreate_msg)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    actual = 7, expected = 12
    recreate_msg = 'To recreate this test in ipython3 run:\n  add_one_and_multiply(5, 2)'

        def check_equals(actual, expected, recreate_msg=None):
            msg = f"Actual ({actual}) and expected ({expected}) values do not match."
            if recreate_msg is not None:
                msg += "\n" + recreate_msg
        
    >       assert actual == expected, msg
    E       AssertionError: Actual (7) and expected (12) values do not match.
    E         To recreate this test in ipython3 run:
    E           add_one_and_multiply(5, 2)
    E       assert 7 == 12
    E         +7
    E         -12

    ../test_utils.py:45: AssertionError
    =============================== short test summary info ================================
    FAILED add_one_and_multiply.py::test_add_one_and_multiply_2 - AssertionError: Actual ...
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ============================= 1 failed, 1 passed in 0.12s ==============================

The volume of output can be a bit overwhelming. You should focus on
the lines towards the end that start with `E`. These lines will
usually contain a helpful message telling you why the test failed:

    E       AssertionError: Actual (7) and expected (12) values do not match.
    E         To recreate this test in ipython3 run:
    E           add_one_and_multiply(5, 2)

This information can help you narrow down the issue with your code.
This error message, in particular, tells you that, like the manual testing
example we saw earlier, the test code expected a return value of 12, but got a return value of 7.  It
also shows you how to run this test in `ipython3`. At this point, you should switch back to testing your
function in `ipython3` until you have fixed the problem.


## Advent of Code

To test whether your solutions are correct, you will need to submit your solution through the [Advent of Code](https://adventofcode.com/) website. Please note that Advent of Code won’t ask you for your code: instead, each problem will ask you to compute a value based on some text-based input. For example, an Advent of Code problem could tell you that the input to the problem looks like this:

    10 20
    37 89
    -7 15
    90 101

The problem could ask you to compute the difference between each pair of numbers, and then produce the largest such different. For example, given the above input, the solution to the problem would be `52` (the difference between `37` and `89`).

To solve an Advent of Code problem, you will need to take the input provided by the Advent of Code website, and save it to a file. For example, we could save the above input to a file called `sample-input.txt`. For each problem, we provide starter code that will parse the input for you, and will call a function in the starter code with those inputs. In other words, you don't have to worry about parsing the input: you just have to implement the function included in the problem's starter code. 

To test your solution with the inputs provided by Advent of Code, you would run your code like this:

    $ python3 aocYYYY-NN.py sample-input.txt

Additionally, each problem is divided into two tasks, and their website will not reveal the second (typically more difficult) task until you solve the first one. Unless we suggest otherwise, we encourage you to try to complete both tasks. Also, while not required by Advent of Code, we encourage you to think about how to define a specific function that will solve each of the tasks, potentially with some additional helper functions, instead of just throwing some code together in IPython.

