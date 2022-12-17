#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 40.py:

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
