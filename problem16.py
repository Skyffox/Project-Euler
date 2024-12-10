# What is the sum of the digits of the number 2^1000?
# Execution time: 0.220s

def power_digit_sum():
    print(sum([int(i) for i in str(2**1000)]))


power_digit_sum()
