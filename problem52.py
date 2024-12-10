# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
# Execution time: 0.247s

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
