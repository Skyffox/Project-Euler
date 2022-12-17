#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 15.py:
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


def numOfRoutes(cubeSize):
    L = [1] * cubeSize
    for i in range(cubeSize):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cubeSize - 1]

print(numOfRoutes(20))
