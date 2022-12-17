#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 82.py:


def _print(matrix):
    for i in matrix:
        print(i)
    print(end="")

f = open('p081_matrix.txt', 'r')

matrix = []
for line in f:
    line = line.strip().split(',')
    line = [int(d) for d in line]
    matrix.append(line)

# matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111],
#             [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]

right_column = [i[len(matrix) - 1] for i in matrix]
start_pos = 0

for counter, val in enumerate(right_column):
    if val == min(right_column):
        start_pos = counter
        break

s = []
for i in range(len(matrix) - 1, 0, -1):
    col = [0] * len(matrix)

    # search above start pos
    for j in range(0, start_pos):
        if i != len(matrix) - 1:
            matrix[j][i] += matrix[j+1][i]
            col[j] += matrix[j][i] + matrix[j][i+1]

    # search below start pos
    for k in range(start_pos + 1, len(matrix)):
        matrix[k][i] += matrix[k-1][i]
        col[k] += matrix[k][i] + matrix[k][i-1]

    # update to the left
    for ii in range(len(matrix)):
        col[ii] = matrix[ii][i-1] + matrix[ii][i]

    for c, x in enumerate(col):
        if x == min(col):
            start_pos = c
            break

    s.append(matrix[start_pos][i])
    if i == 1:
        # update to the left
        for ii in range(len(matrix)):
            col[ii] = matrix[ii][i-1] + matrix[ii][i]

        for counter, val in enumerate(col):
            if val == min(col):
                start_pos = counter
                s.append(matrix[start_pos][i-1])
                break


print("Minimal sum", sum(s))
