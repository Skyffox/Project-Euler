# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
# Execution time: ???

BOUND = 51
total = 0
xs = []
for px in range(0, BOUND):
    for py in range(0, BOUND):
        if px == 0 and py == 0:
            continue
        for qx in range(0, BOUND):
            for qy in range(0, BOUND):
                if [px, py] == [qx, qy]:
                    continue
                if qx == 0 and qy == 0:
                    continue
                if [qx, qy, px, py] in xs:
                    continue

                xs.append([px, py, qx, qy])
                p1 = ((px)**2 + (py)**2)**0.5 # p to 0
                p2 = ((qx)**2 + (qy)**2)**0.5 # q to 0
                p3 = ((px - qx)**2 + (py - qy)**2)**0.5 # p to q

                m = max([p1, p2, p3])

                if m == p1:
                    if (int(p2**2 + p3**2) == int(p1**2)):
                        total += 1
                elif m == p2:
                    if (int(p1**2 + p3**2) == int(p2**2)):
                        total += 1
                else:
                    if (int(p1**2 + p2**2) == int(p3**2)):
                        total += 1

print("Total right triangles", total)
