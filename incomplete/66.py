# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
# Equation: x^2 - Dy^2 = 1
# Execution time: ???

# See:
# http://en.wikipedia.org/wiki/Chakravala_method#The_method
# http://kappadath-gopal.blogspot.com/2013/04/ancient-medieval-indian-mathematics.html

import math

largest_x = 0
result = 0

for D in range(2, 100):
    tmp = 0
    solution = False

    # A perfect square is a number that can be expressed as the product of two equal integers.
    if not (math.sqrt(D) - int(math.sqrt(D))):
        # It is now a perfect square, we know that when D is a perfect square there is no solution.
        continue

    # One of the solution methods is by calculating the convergents of the square root of D.
    # # So if n/d is the ith convergent of the square root of D then it is the minimal
    # # solution h - D*d = 1 to the equation.

    m = 0
    d = 1
    a = D**0.5

    n_1 = 1
    num = a

    d_1 = 0
    denum = 1

    # Calculating the convergents
    while (num*num - D*denum*denum) != 1:
        m = d * a - m
        d = (D - m * m) / d
        a = (math.sqrt(D) + m) / d

        num2 = n_1
        n_1 = num

        denum2 = d_1
        d_1 = denum

        num = a*n_1 + num2
        denum = a*d_1 + denum2

    if num > largest_x:
        largest_x = num
        result = D


print("The largest x-value is:", largest_x)



