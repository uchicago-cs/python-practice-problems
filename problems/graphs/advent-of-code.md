# Advent of Code: Graphs

We suggest working through the following Advent of Code problems:

## 2019: Day #6

- [Problem statement](https://adventofcode.com/2019/day/6)
- [Starter code](aoc2019-06.py)

Hint: Part 2 can be solved with BFS, but requires converting
the provided `orbits` dictionary into an actual graph data structure.

## 2020: Day #7

- [Problem statement](https://adventofcode.com/2020/day/7)
- [Starter code](aoc2020-07.py)

Hint: Use either DFS or BFS in Part 1 to determine whether one
color is reachable from another.

## 2021: Day #9

- [Problem statement](https://adventofcode.com/2021/day/9)
- [Starter code](aoc2021-09.py)

Hint: Part 2 involves doing [flood filling](https://en.wikipedia.org/wiki/Flood_fill),
a type of graph traversal that is similar to DFS (but which can also be implemented
using BFS)

## 2022: Day #12

- [Problem statement](https://adventofcode.com/2022/day/12)
- [Starter code](aoc2022-12.py)

Hint: Part 1 involves using BFS to find the shortest path. Also, take into account
that you can use Python's built-in `ord()` function to convert a character into
an integer that preserves the ordering of the characters (e.g., `ord("a")` will produce
an integer that is less than `ord("b")`)