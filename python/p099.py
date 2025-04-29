# Determine which line number has the greatest numerical value.
# Execution time: 0.250s

import math

f = open("inputs/p099_base_exp.txt", "r")

best_line = 1
for it, line in enumerate(f):
    line = line.strip().split(",")
    line = [int(i) for i in line]

    if it == 0:
        n1 = line[1] * math.log(line[0])
        continue

    n2 = line[1] * math.log(line[0])

    if n2 > n1:
        n1 = n2
        best_line = it + 1

print(best_line)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
