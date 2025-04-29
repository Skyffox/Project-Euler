def solution(N):
    n = 2
    prev_n = 1
    
    fract = 1
    for k in range(2, N+1):
        temp = prev_n
        if (k % 3 == 0):
            fract = 2 * int(k/3)
        else:
            fract = 1
        prev_n = n
        n = fract * prev_n + temp
    
    sum = digit_sum(n)
    print(sum)
    

def digit_sum(num):
    sum = 0
    while num > 0:
        sum = sum + (num % 10)
        num = num // 10
    return sum


solution(100)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")


# The code is pretty straightforward. We only need to keep track of the two most recent numerators. The variables n and prev_n are used to keep track of the last two numerators. The continuous fraction is 
# 1
# 1
#  if k % 3 is not 
# 0
# 0
#  and 
# 2
# k
# 2k
#  is k % 3 is 
# 0
# 0
# . This ensures that for each group of three consecutive values of 
# k
# k
# , one of them evaluates to 
# 2
# k
# 2k
# .

# Next, we update prev_n to the current value of n and store the value of prev_n in the temp variable to calculate the new value of n, our next numerator.

# Lastly, the sum_digit() function takes in a number and returns the sum of its digits.