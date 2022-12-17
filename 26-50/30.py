#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 30.py:
# Find the sum of all the numbers that can be written as the sum of fifth powers
# of their digits.

# Highest possile number.
roof = 5 * 9**5
result = 0

for i in range(2, roof):
	s = 0
	number = i

	while number > 0:
		# Get last number of the big number.
		d = number % 10
		# Divide by ten to get the second last number next time.
		number = int(number / 10)

		s += d**5

	if s == i:
		result += i

print(result)
