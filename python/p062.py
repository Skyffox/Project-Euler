# Find the smallest cube for which exactly five permutations of its digits are cube.
# Execution time: 9.221s

# Create the cubes
cubes = [x**3 for x in range(9000)]

# Compare the lenght of both cubes then sort the strings to see if it is a permutation.
for i, cube1 in enumerate(cubes):
    lst_cube1 = list(str(cube1))
    permutations = [cube1]

    for cube2 in cubes[i+1:]:
        lst_cube2 = (str(cube2))

        if len(lst_cube2) < len(lst_cube1):
            continue

        if len(lst_cube2) > len(lst_cube1):
            break

        if sorted(lst_cube1) == sorted(lst_cube2):
            permutations.append(cube2)

    if len(permutations) == 5:
        break

print("Digits with 5 permutations:", permutations)

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
