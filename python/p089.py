# Find the number of characters saved by writing each of these in their minimal form.
# Execution time: 0.252s

literals = {"I" : 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000 }


f = open('inputs/p089_roman.txt', 'r')
total_saved = 0
for line in f:
    line = line.strip()
    lit = [str(c) for c in line]

    s = 0
    for it, ele in enumerate(lit):
        try:
            if ele == "I" and (lit[it+1] == "V" or lit[it+1] == "X"):
                s -= 1
                continue

            if ele == "X" and (lit[it+1] == "L" or lit[it+1] == "C"):
                s -= 10
                continue

            if ele == "C" and (lit[it+1] == "D" or lit[it+1] == "M"):
                s -= 100
                continue
        except:
            pass

        s += literals[ele]

    m = 0
    d = 0
    c = 0
    l = 0
    x = 0
    v = 0
    i = 0

    while s >= 1000:
        m += 1
        s -= 1000

    if s >= 900:
        c += 1
        m += 1
        s -= 900

    while s >= 500:
        d += 1
        s -= 500

    if s >= 400:
        c += 1
        d += 1
        s -= 400

    while s >= 100:
        c += 1
        s -= 100

    if s >= 90:
        x += 1
        c += 1
        s -= 90

    while s >= 50:
        l += 1
        s -= 50

    if s >= 40:
        x += 1
        l += 1
        s -= 40

    while s >= 10:
        x += 1
        s -= 10

    if s >= 9:
        i += 1
        x += 1
        s -= 9

    while s >= 5:
        v += 1
        s -= 5

    if s >= 4:
        i += 1
        v += 1
        s -= 4

    while s >= 1:
        i += 1
        s -= 1

    total_saved += (len(lit) - (m + d + c + l + x + v + i))

print(total_saved)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
