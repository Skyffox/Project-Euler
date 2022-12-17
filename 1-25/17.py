#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 17.py:
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# Amount of letters in single digits and numbers from 10 to 19.
S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
# Amount of letters in tens
D = [0,3,6,6,5,5,5,7,6,6]
H = 7 # Hundred
T = 8 # Thousand
 
total = 0
for i in range(1, 1000):
    c = i % 10 # Single digit
    b = ((i % 100) - c) / 10 # Tens digit
    a = ((i % 1000) - (b * 10) - c) / 100 # Hundreds digit
 
    if a != 0:
        total += S[int(a)] + H # S[a] hundred
        if b != 0 or c != 0:
            total += 3 # "and"
    if b == 0 or b == 1:
        total += S[int(b * 10 + c)]
    else:
        total += D[int(b)] + S[int(c)]
 
total += S[1] + T
print (total)
