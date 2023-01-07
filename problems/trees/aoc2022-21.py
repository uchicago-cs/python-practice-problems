"""
Starter code for Advent of Code 2022 Day #21

You must implement functions part1 and part2
"""

import sys
import os


def part1(monkeys):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - monkeys: A dictionary mapping monkey names to a list of
      strings representing what the monkey "shouts".
      If the list contains a single string, it will represent
      an integer. If it contains three strings, it represents
      an arithmetic operation. For example:

        {'root': ['pppw', '+', 'sjmn'],
         'dbpl': ['5'],
         'cczh': ['sllz', '+', 'lgvd']}

    Returns an integer
    """

    ### Replace with your code
    return None


def part2(monkeys):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - monkeys: Same as Part 1.

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
        lines = [line.split(": ") for line in f.read().split("\n")]
        monkeys = {}
        for monkey, message in lines:
            monkeys[monkey] = message.split()

    print(f"Part 1:", part1(monkeys))
    
    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", part2(monkeys))
