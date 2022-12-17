# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# Execution time: 0.289s

def champernowne(last):
    ans = ""
    for c in range(last):
        ans += str(c)
    return ans

champ = champernowne(200000)
answer = 1
for c in range(6):
    answer *= int(champ[10**c])

print (answer)
