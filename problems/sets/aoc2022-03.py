"""
Starter code for Advent of Code 2022 Day #3

You must implement function sum_priorities
"""

import sys
import os


def sum_priorities(rucksacks, group_size=None):
    """
    Given a list of rucksacks, divide them up into groups
    find the common element in each group, and add up the
    priorities of each common element.

    Parameter:
    - rucksacks (list of strings)
    - group_size (integer): The number of rucksacks in each
      group. If None, then each group will contain the two
      halves of a rucksack (i.e., if this parameter is None,
      you are solving Part 1 of the problem)

    Returns an integer
    """

    ### Replace with your code
    return None


############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###         to the function above        ###
###                                      ###
############################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        rucksacks = [x for x in f.read().split()]

    print(f"Part 1:", sum_priorities(rucksacks))
    
    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", sum_priorities(rucksacks, 3))
