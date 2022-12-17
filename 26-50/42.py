#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 42.py:

def triangle_number(word_val):
    n = 1
    while True:
        triangle_n = 0.5 * n * (n + 1)
        if triangle_n == word_val:
            return True
        if triangle_n > word_val:
            return False
        n += 1


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
triangle_words = 0
word_value = 0
with open("p042_words.txt", "r") as f:
    data=f.read().replace('\n', '')
    for letter in data:
        if letter in letters:
            for i, find_letter in enumerate(letters):
                if letter == find_letter:
                    word_value += (i+1)
                    break
        else:
            if triangle_number(word_value):
                triangle_words += 1
            word_value = 0

print ("Amount of triangle words in the file:", triangle_words)
