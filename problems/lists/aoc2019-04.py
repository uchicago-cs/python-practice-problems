"""
Starter code for Advent of Code 2019 Day #4

You must implement functions is_valid and 
count_valid_passwords.

NOTE: In this problem, the input to the problem
is just two integers, so Advent of Code did not
provide input files. Instead of specifying
an input file when running this code, you should
instead set the MIN_VALUE and MAX_VALUE variables
(see below) and run the code like this:

    python3 aoc2019-04.py
"""

import sys
import os

# Update with the range specified in the problem
MIN_VALUE=0
MAX_VALUE=0


def is_valid(password, require_standalone_pair):
    """
    Checks whether a password is valid.

    Parameters:
    - password (integer): The password to check
    - require_standalone_pair (boolean): If True, 
      then any pair of adjacent digits must be 
      by themselves (not part of a longer sequence 
      of matching digits). Note: You can ignore
      this parameter when implementing Part 1 of
      the problem.

    Returns a boolean (True if the password if valid,
    False otherwise)
    """

    ### Replace with your code
    return None


def count_valid_passwords(lb, ub, require_standalone_pair):
    """
    Count the number of valid passwords in a given range

    Parameters:
    - lb, ub (integers): The lower and upper bound
      (inclusive) of the range of passwords.
    - require_standalone_pair (boolean): See is_valid()
      docstring.

    Returns an integer (the number of valid passwords)
    """

    ### Replace with your code
    return None


############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

if __name__ == "__main__":
    print(f"Part 1:", count_valid_passwords(MIN_VALUE, MAX_VALUE, False))

    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", count_valid_passwords(MIN_VALUE, MAX_VALUE, True))
