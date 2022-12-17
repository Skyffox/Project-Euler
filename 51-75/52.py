#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 52.py:

def same(x, a, b):
    if sorted(set(str(a*x))) == sorted(set(str(b*x))):
        return True
    return False

x = 125874
while True:
    x += 1
    if same(x,1,2) and same(x,2,3) and same(x,3,4) and same(x,4,5) and same(x,5,6):
        print (x)
        break
