# How many Lychrel numbers are there below ten-thousand?
# Execution time: 0.263s

def palindrome(num):
    return str(num) == str(num)[::-1]


lynchrel_nums = 0
for n in range(10000):
    is_palindrome = 0
    for it in range(51):
        reverse = int(str(n)[::-1])
        num = n + reverse
        if palindrome(num):
            is_palindrome = 1
            break
        n = num
    if is_palindrome == 0:
        lynchrel_nums += 1
    
print (lynchrel_nums)
