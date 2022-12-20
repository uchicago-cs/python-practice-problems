# Be-a-Computer: Recursion

In the following exercises, you will be shown a piece of code, and will have to figure out what it does (without running it yourself in the Python interpreter)


## Exercise #1

What is the output of the following code?

    def mystery(a, b, c, d):
        if c == 0:
            return d
        elif c % 2 == 0:
            return b + mystery(a, b, c - 2, d)
        else:
            return a + mystery(a, b, c - 1, d)

    print("Result:")
    print(mystery("x", "y", 6, "z"))
    print(mystery("x", "y", 5, "z"))
    print()


## Exercise #2

What is the output of the following code?

    def flip(s, a):
        if a == 0:
            return s
        for i in range(a):
            if s[i] == "*":
                s[i] = "-"
            else:
                s[i] = "*"
        return flip(s, a//2)

    print("Result:")
    s = []
    for i in range(64):
        s.append("*")
    s = flip(s, 64)
    t = ""
    for c in s:
        t = t + c
    print(t)


## Exercise #3

What is the output of the following code?

    def mystery2(N):
        if N < 1:
            return
        mystery2(N-1)
        print(N)
        mystery2(N-2)

    print("Result:")
    mystery2(4)

## Exercise #4

This exercise is a bit more challenging than the previous ones. What is the output of the following code?

    def mystery3(s, c, d, x):
        if s == "":
            return x
        elif s[0] == c:
            return mystery3(s[1:], c, d, x+1)
        elif s[0] == d:
            if x > 0:
                return mystery3(s[1:], c, d, x-1)        
            return -1
        else:
            return mystery3(s[1:], c, d, x)


    def recursion_warmup():
        output_str = 'mystery3("{}", "a", "b", 0): {}'
        for s in ["ab", "abab", "abaab", "ababb", "ababaa"]:
            print(output_str.format(s,  mystery3(s, "a", "b", 0)))

    print("Result:")
    recursion_warmup()