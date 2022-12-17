# Find the maximum total from top to bottom in triangle with one-hundred rows.
# Execution time: 0.260s

t = []
with open('inputs/p067_triangle.txt', 'r') as f:
    for line in f:
        line = line.strip().split(' ')
        t.append([int(x) for x in line])


# Work from bottom to top, minus two for bottom and top row.
for i in range(len(t) - 2, -1, -1):
    # Just a fancy way to iterate over the length of the line.
    for j in range(i+1):
        t[i][j] += max(t[i + 1][j], t[i + 1][j + 1])


print('Maximum path:', t[0][0])
