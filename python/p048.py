# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
# Execution time: 0.223s

total = 0
for x in range(1, 1001):
    total += (x**x)

lst = list(str(total))
digits = lst[-10:]
ans = int(''.join(digits))
print (ans)

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
