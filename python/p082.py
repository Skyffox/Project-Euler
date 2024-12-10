matrix = [[131, 673, 234, 103, 18],
          [201, 96, 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956],
          [805, 732, 524, 37, 331]]

first_cells = [(matrix[x][0], x) for x, _ in enumerate(matrix)]
highest = max([max(x) for x in matrix]) + 1

finish = len(matrix)
paths = []

for num in first_cells:
    x = num[1]
    y = 0

    path = [matrix[x][y]]

    while y != finish - 1:
        right = matrix[x][y + 1]

        if right in path:
            right = highest

        top = highest
        bottom = highest

        if x > 0:
            top = matrix[x - 1][y]
            if top in path:
                top = highest
        if x < len(matrix) - 1:
            bottom = matrix[x + 1][y]
            if bottom in path:
                bottom = highest

        least = min(right, top, bottom)
        if least == right:
            path.append(right)
            y += 1
        elif least == top:
            path.append(top)
            x -= 1
        elif least == bottom:
            path.append(bottom)
            x += 1

    paths.append(path)


s = highest * len(matrix)
shortest_path = []
for p in paths:
    tmp = sum(p)
    if tmp < s:
        s = tmp
        shortest_path = p

print(s, shortest_path)