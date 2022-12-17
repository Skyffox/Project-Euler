# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# Execution time: 0.250s

def fib_seq(x, y, counter):
    while len(str(y)) < 1000:
        tmp = y
        y = y + x
        x = tmp
        counter += 1

    return counter


print(fib_seq(1, 1, 2))
