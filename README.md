# Python Practice Problems

This repository contains a collection of Python practice problems, primarily intended for students taking CMSC 14100 and CMSC 14200 at the University of Chicago.

| Category            | Be-a-Computer                                           | Short Exercises                                             | Advent of Code                                            |
|---------------------|---------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------|
| Loops               | [Be-a-Computer](problems/loops/be-a-computer.md)        | [Short Exercises](problems/loops/short-exercises.md)        | [Advent of Code](problems/loops/advent-of-code.md)        |
| Sets                | [Be-a-Computer](problems/sets/be-a-computer.md)         | [Short Exercises](problems/sets/short-exercises.md)         | [Advent of Code](problems/sets/advent-of-code.md)         |
| Dictionaries        | [Be-a-Computer](problems/dictionaries/be-a-computer.md) | [Short Exercises](problems/dictionaries/short-exercises.md) | [Advent of Code](problems/dictionaries/advent-of-code.md) |
| Classes and Objects | [Be-a-Computer](problems/oo/be-a-computer.md)           | [Short Exercises](problems/oo/short-exercises.md)           | [Advent of Code](problems/oo/advent-of-code.md)           |
| Recursion           | [Be-a-Computer](problems/recursion/be-a-computer.md)    | [Short Exercises](problems/recursion/short-exercises.md)    | [Advent of Code](problems/recursion/advent-of-code.md)    |
| Trees               | [Be-a-Computer](problems/trees/be-a-computer.md)        | [Short Exercises](problems/trees/short-exercises.md)        | [Advent of Code](problems/trees/advent-of-code.md)        |
| Graphs              | [Be-a-Computer](problems/graphs/be-a-computer.md)       | [Short Exercises](problems/graphs/short-exercises.md)       | [Advent of Code](problems/graphs/advent-of-code.md)       |
| Challenge Problems  | [Be-a-Computer](problems/challenge/be-a-computer.md)    | [Short Exercises](problems/challenge/short-exercises.md)    | [Advent of Code](problems/challenge/advent-of-code.md)    |

Each category targets a topic covered somewhere in CMSC 14100 or CMSC 14200, except the "Challenge Problems" category, which target general problem-solving skills (including selecting the right data structure to solve the problem)

We provide three types of practice problems:

- **Be-a-Computer**: In these problems, you will be presented with a piece of code, and must figure out what the code does (without running the code itself in the Python interpreter)
- **Short Exercises**: Short coding exercises where you must write a piece of code to perform a specific task.
- **Advent of Code**: Curated list of [Advent of Code](https://adventofcode.com/) problems (see below for more details)

Some problems may provide some starter code, which will be linked from the problem description.

## Suggested Usage of this Repository

To work through the problems in this repository, we suggest you first create a *fork* of this repository. This will create a copy (or "fork") of this repository under your personal GitHub account, which will allow you to push your solutions to your fork.

To create a fork, make sure you are in the repository's root on GitHub (https://github.com/uchicago-cs/python-practice-problems) and then click on the "Fork" button on the top-left. This wil take you to a page with a number of options; leave everyting as-is and click "Create fork". You can see more detailed instructions on GitHub's [Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) documentation.

Once you have created your fork of the repository, we suggest creating a top-level `solutions/` directory, mimicking the structure of the `problems/` directory. For example, you would place your solutions to the Recursion problems inside `solutions/recursion/`. If a problem provides some starter code, we recommend copying the starter code into the corresponding `solutions/` directory (instead of editing the starter code itself)

Following these guidelines will ensure that your solutions are all in the same place, and can more easily be found by anyone looking at your repository.

Please note that, since these practice problems are not graded, you are welcome to make your forked repository public, and to share and discuss solutions with other students. You can also use it as a portfolio of code you've written, which can be shared with prospective employers.

## Advent of Code problems

Some of the problems we provide are a curated list of problems from [Advent of Code](https://adventofcode.com/), a yearly set of programming puzzles that are released in an [advent calendar](https://en.wikipedia.org/wiki/Advent_calendar) schedule.

To test whether your solutions are correct, you will need to submit your solution through the Advent of Code website. Please note that Advent of Code won’t ask you for your code: instead, each problem will ask you to compute a value based on some inputs (you can think of it as there being a single automated test that determines whether your solution is correct or not) Additionally, each problem is divided into two tasks, and their website will not reveal the second (typically more difficult) task until you solve the first one. Unless we suggest otherwise, we encourage you to try to complete both tasks. 

For each problem, we provide starter code that will parse the input for you, and will call a function in the starter code with those inputs. In other words, you don't have to worry about parsing the input: you just have to implement the function included in the problem's starter code. To test your solution with the inputs provided by Advent of Code, save the input into a file (e.g., `sample-input.txt`) and then run your code like this:

    $ python3 aocYYYY-NN.py sample-input.txt

One reason we have selected these problems is because Advent of Code participants are encouraged to share their solutions broadly, which means that, once you've written your own solution, you can look at other published solutions online to learn about the different ways of approaching a problem. You can find solutions written by a UChicago CS instructor, Prof. Borja Sotomayor, in his [Advent of Code repository](https://github.com/borjasotomayor/advent-of-code/). Advent of Code also has a very active [subreddit](https://www.reddit.com/r/adventofcode/) with lots of information about solutions, strategies, etc.

Finally, it you're looking to build a code portfolio that you can share with employers, we recommend creating a separate GitHub repository for your Advent of Code solutions (not just the ones we recommend here). Advent of Code is a sufficiently well-known event that many employers will appreciate being able to see your solutions to those problems.
