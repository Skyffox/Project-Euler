# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Execution time: 0.725s

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

sum = 0
for x in range(3, 100000):
    lst = list(str(x))
    tot = 0
    for num in lst:
        tot += factorial(int(num))

    if tot == x:
        sum += x
        
print ("Total for curious numbers:", sum)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
