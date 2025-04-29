# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and
# D = |Pk − Pj| is minimised; what is the value of D?
# Execution time: 680.583s

n = 10000
p_num = [i * (3*i - 1) / 2 for i in range(1, n)]
D = p_num[-1]
b = False
for i, x in enumerate(p_num):
    for y in p_num[i+1:]:
        if x + y in p_num and y - x in p_num:
            D = abs(y - x)
            b = True
            break
    if b:
        break

print("Minimised difference:", D)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
