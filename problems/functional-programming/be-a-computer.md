# Be-a-Computer: Functional Programming

In the following exercises, you will be shown a piece of code, and will have to figure out what it does (without running it yourself in the Python interpreter)


## Exercise #1

What is the output of the following code?

    def functional_programming_warmup():
        return map(lambda x: x + 1, 
                filter(lambda x: x % 3 == 0, range(0, 9)))

    print("Result:")
    l = functional_programming_warmup()
    print(list(l))


## Exercise #2

What is the output of the following code?

    def mystery2(fn, N):
        def g(x):
            for i in range(N):
                x = fn(x)
            return x
        return lambda y: g(y*2)


    print("Result:")
    f = mystery2(lambda x: x+1, 10)
    print(f(10))


## Exercise #3

What is the output of the following code?

    def gen_fn(c):
        def fn(x):
            return x % c == 0
        return fn

    print("Result:")
    print(list(filter(gen_fn(10), map(lambda x: x * 2, [10, 25, -10, 18, -9]))))
    print(list(map(lambda x: x * 2, filter(gen_fn(5), [10, 25, -10, 100, -9]))))

