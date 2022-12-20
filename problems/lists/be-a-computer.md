# Be-a-Computer: Lists

In the following exercises, you will be shown a piece of code, and will have to figure out what it does (without running it yourself in the Python interpreter)


## Exercise #1

What is the output of the following code?

    def mystery1(l):
        rv = []
        for x in l:
            rv = [x] + rv
        return rv

    print("Result:")
    l = [0, 1, 2, 3, 4]
    nl = mystery1(l)
    print("l: ", l)
    print("nl: ", nl)


## Exercise #2

What is the output of the following code?

    def mystery1(l):
        rv = []
        for x in l:
            rv = [x] + rv
        return rv

    print("Result:")
    l = [0, 1, 2, 3, 4]
    nl = mystery1(l)
    print("l: ", l)
    print("nl: ", nl)


## Exercise #3

What is the output of the following code?

    def mystery2(l):
        rv = []
        for i in range(len(l)-1, -1, -1):
            rv.append(l[i])
        return rv

    print("Result:")
    l = [0, 1, 2, 3, 4]
    nl = mystery2(l)
    print("l: ", l)
    print("nl: ", nl)


## Exercise #4

This exercise is a bit more challenging than the previous ones. What is the output of the following code?

    def mystery3(l):
        n = len(l)
        for i in range(n // 2):
            t = l[i]
            l[i] = l[n-i-1]
            l[n-i-1] = t

    print("Result:")
    l = [0, 1, 2, 3, 4]
    mystery3(l)
    print("l: ", l)