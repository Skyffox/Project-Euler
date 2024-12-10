# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}. For which value of p ≤ 1000, is the number of solutions maximised?
# Execution time: 133.845s

def perimeter(p):
    solutions = 0
    for a in range(p):
        for b in range(a+1, p):
            c = p - (a + b)
            if a+b+c == p and a**2 + b**2 == c**2:
                solutions += 1
    return solutions

max_s = 0
max_p = 0
for p in range(1, 1001):
    solutions = perimeter(p)

    if solutions > max_s:
        max_s = solutions
        max_p = p

print ("Number of solutions maximised for:", max_p)
