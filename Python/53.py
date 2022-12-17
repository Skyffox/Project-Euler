# How many, not necessarily distinct, values of combinations for 1 <= n <= 100 are greater than one-million?
# Execution time: 0.325s

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
def combinatorics(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
        
vals = 0
for n in range(1, 101):
    for r in range(n+1):
        if combinatorics(n, r) > 1000000:
            vals += 1
    
print (vals)
