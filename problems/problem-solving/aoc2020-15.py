"""
Starter code for Advent of Code 2020 Day #15

You must implement function memory_game
"""

import sys
import os


def memory_game(numbers, n):
    """
    Given a list of numbers, determine what will be
    the n-th number spoken (according to the memory
    game)

    Parameter:
    - numbers (list of integers)
    - n (integer)

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
        numbers = [int(x) for x in f.read().strip().split(",")]

    print(f"Part 1:", memory_game(numbers, 2020))
    
    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", memory_game(numbers, 30000000))
