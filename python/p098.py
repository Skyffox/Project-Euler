
# By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. 
# What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962.
# What is the largest square number formed by any member of such a pair?

# To solve this problem, we need to:
# Convert each word into a unique representation (for example, sort the characters or use a signature like the sum of the characters' ASCII values).
# Map those representations to square numbers.
# Check for pairs of square numbers whose corresponding words are anagrams of each other.
# Find the largest square number among these pairs.

# Solution Strategy:
# Generate Square Numbers: First, we'll generate a list of square numbers, as they will form the basis for checking the anagram pairs.
# Sort and Check Anagrams: For each word, sort its letters and use this sorted string as a signature. This will help identify which words are anagrams of each other.
# Map Words to Square Numbers: For each anagram group, check if they correspond to valid square numbers. We can do this by verifying if the numbers formed by the sorted letters of a word are perfect squares.
# Find the Largest Pair: Among the valid anagram pairs of square numbers, find the largest square.

# Execution time: ???

import math

def is_perfect_square(n):
    """Check if a number n is a perfect square."""
    return int(math.sqrt(n)) ** 2 == n

# Strings a and b must be anagrams of each other.
def max_square_pair(a, b, index, assignments, isdigitused):
	if index == len(a):
		if      a[0] in assignments and assignments[a[0]] == 0 or \
		        b[0] in assignments and assignments[b[0]] == 0:
			return 0
		
		anum = 0
		bnum = 0
		for (x, y) in zip(a, b):
			anum = anum * 10 + assignments[x]
			bnum = bnum * 10 + assignments[y]
		if is_perfect_square(anum) and is_perfect_square(bnum):
			return max(anum, bnum)
		else:
			return 0
	
	elif a[index] in assignments:
		return max_square_pair(a, b, index + 1, assignments, isdigitused)
	
	else:
		result = 0
		for i in range(10):
			if not isdigitused[i]:
				isdigitused[i] = True
				assignments[a[index]] = i
				result = max(max_square_pair(a, b, index + 1, assignments, isdigitused), result)
				del assignments[a[index]]
				isdigitused[i] = False
		return result

def compute():
	with open("inputs/p098_words.txt", "r", encoding="utf-8") as file:
		anagrams = {}
		for words in file:
			words = words.strip().split(",")
			for word in words:
				word = word.replace("\"", "")
				print(word)
				key = "".join(sorted(word))
				if key not in anagrams:
					anagrams[key] = []
				anagrams[key].append(word)

	ans = 0
	for (key, words) in anagrams.items():
		for i in range(len(words)):
			for j in range(i + 1, len(words)):
				assignments = {}
				ans = max(max_square_pair(words[i], words[j], 0, assignments, [False] * 10), ans)
	return str(ans)

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
