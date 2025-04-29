# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
# Execution time: 0.341s

largest_s = 0
for a in range(101):
    for b in range(101):
        n = a**b
        lst = [int(x) for x in str(n)]
        s = sum(lst)
        
        if s > largest_s:
            largest_s = s

print (largest_s)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
