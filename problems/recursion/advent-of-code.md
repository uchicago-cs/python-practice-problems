# Advent of Code: Recursion

We suggest working through the following Advent of Code problems:

## 2020: Day #10

- [Problem statement](https://adventofcode.com/2020/day/10)
- [Starter code](aoc2020-10.py)

Note: Recursion is required in Part 2 of the problem, not in Part 1
(but you'll need to solve Part 1 to unlock Part 2). Also, fully solving this 
problem is challenging, but there are some intermediate steps that 
should be doable and are good recursion practice.

More specifically, we encourage you to approach this task as simply writing a recursive function to recursively generating the “arrangement of jolts”, as that is representative of the kinds of recursion problems in an introductory programming class.

However, while you will be able to test your solution with the smaller test cases shown in the problem, writing a function that generates the arrangements won’t work for the larger test cases, which involve **trillions** of arrangements. This requires a much more clever solution focused on *counting* the arrangements without generating them. We encourage you to think about how to do this as well, and it should be possible for you to come up with a recursive counting algorithm that works for the small test cases (but, again, fully solving the problem is challenging, so don't be discouraged if you can't do it)
