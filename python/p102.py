# Find the number of triangles for which the interior contains the origin.
# Execution time: ???

total = 0

with open("p102_triangles.txt") as file:
    for line in file:
        coords = line.strip().split(",")
        if len(coords) != 6:
            break
        coords = [int(x) for x in coords]

        # Take x and y coordinates.
        xcoords = coords[::2]
        ycoords = coords[1::2]

        # Check if coordinates fall in correct quadrant.
        if max(xcoords) > 0 > min(xcoords) and max(ycoords) > 0 > min(ycoords):
            index = 0
            upper_bound = False
            lower_bound = False

            inter1 = (ycoords[0] - ycoords[1]) / (xcoords[0] / xcoords[1])
            inter2 = (ycoords[0] - ycoords[2]) / (xcoords[0] / xcoords[2])
            inter3 = (ycoords[1] - ycoords[2]) / (xcoords[1] / xcoords[2])

            print(inter1, inter2, inter3)


            # y_max = max(ycoords)
            #
            # # Go over other coordinates to check where they intersect.
            # for idx, j in enumerate(ycoords):
            #     if j == y_max:
            #         continue
            #
            #     if xcoords[idx] > 0:
            #         if (ycoords[idx] - ycoords[index]) / (xcoords[idx] / xcoords[index]) > 0:
            #             upper_bound = True
            #     else:
            #         if (ycoords[idx] - ycoords[index]) / (xcoords[idx] / xcoords[index]) < 0:
            #             lower_bound = True
            #
            # if upper_bound and lower_bound:
            #     total += 1

        break


print("Total of origins in triangle:", total)
