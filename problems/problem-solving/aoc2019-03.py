"""
Starter code for Advent of Code 2019 Day #3

You must implement functions part1 and part2
"""

import sys
import os


def part1(wire1, wire2):
    """
    Solves Part 1 (see problem statement for more details)

    Parameters:
    - wire1, wire2 (list of (str,int) pairs): Each entry
      of the list is a (direction, distance) tuple.

    Returns an integer
    """

    ### Replace with your code
    return None


def part2(wire1, wire2):
    """
    Solves Part 2 (see problem statement for more details)

    Parameters:
    - wire1, wire2 (list of (str,int) pairs): Each entry
      of the list is a (direction, distance) tuple.

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
        input = [x for x in f.read().split()]
        if len(input) != 2:
            print(f"ERROR: Input file must contain two lines only")
            sys.exit(1)
        
        wires = []
        for line in input:
            wire = [(x[0], int(x[1:])) for x in line.split(",")]
            wires.append(wire)
        wire1, wire2 = wires

    print(f"Part 1:", part1(wire1, wire2))
    
    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", part2(wire1, wire2))
