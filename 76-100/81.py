#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 81.py:

f = open('p081_matrix.txt', 'r')

matrix = []
for line in f:
    line = line.strip().split(',')
    line = [int(d) for d in line]
    matrix.append(line)


for i in range(len(matrix) - 2, -1, -1):
    matrix[len(matrix) - 1][i] += matrix[len(matrix) - 1][i+1]
    matrix[i][len(matrix) - 1] += matrix[i+1][len(matrix) - 1]


for i in range(len(matrix) - 2, -1, -1):
    for j in range(len(matrix) - 2, -1, -1):
        matrix[i][j] += min(matrix[i][j+1], matrix[i+1][j])


print("Minimal sum", matrix[0][0])
