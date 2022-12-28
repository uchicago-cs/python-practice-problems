"""
Starter code for Advent of Code 2020 Day #1

You must implement functions part1 and part2
"""

import sys
import os


def part1(numbers):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
    """

    ### Replace with your code
    return None


def part2(numbers):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
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
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        numbers = [int(x) for x in f.read().split()]

    print(f"Part 1:", part1(numbers))

    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", part2(numbers))
