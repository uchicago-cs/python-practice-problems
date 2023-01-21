"""
Starter code for Advent of Code 2020 Day #7

You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(rules):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - rules: a dictionary mapping colors to a list
             of (color, amount)

    Returns an integer
    """
    ### Replace with your code
    return None


def part2(rules):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - rules: a dictionary mapping colors to a list
             of (color, amount)

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

def read_rules(lines):
    """
    Given the text input, convert it to a graph-like structure.
    Specifically, a dictionary mapping colors to a list of (color, amount)
    tuples.
    """

    rules = {}

    for line in lines:
        m = re.match("(.*) bags contain (.*)\.", line)
        container_bag, contained_bags = m.groups()

        if contained_bags == "no other bags":
            bags = []
        else:
            bags = []
            bag_strs = contained_bags.split(", ")
            for bag in bag_strs:
                amount, color1, color2, _ = bag.split()
                bags.append((f"{color1} {color2}", int(amount)))

        rules[container_bag] = bags

    return rules

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        lines = f.read().strip().split("\n")
        rules = read_rules(lines)

    print(f"Part 1:", part1(rules))
    
    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", part2(rules))
