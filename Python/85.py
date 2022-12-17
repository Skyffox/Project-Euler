# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.
# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
# Execution time: 7.679s

def approx(x, y):
    total = x*y + 1 + x + y
    t = 0
    for i in range(1, x+1):
        for j in range(1, y+1):
            # exclude what we already have defined above
            if (i == 1 and j == 1) or (i == 1 and j == y) or (j == 1 and i == x) or (i == x and j == y):
                continue
            x_diff = x - i + 1
            y_diff = y - j + 1
            t += (x_diff * y_diff)

    return total + t


BOUND = 2000000
min = BOUND
best_i = 0
best_j = 0
for i in range(3, 120):
    for j in range(i, 120):
        p = abs(BOUND - approx(i, j))
        if p < min:
            min = p
            best_i = i
            best_j = j

print("Best i and j:", best_i, best_j)
print("Area then is:", best_i * best_j)
