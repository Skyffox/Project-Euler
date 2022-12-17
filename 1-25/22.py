#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 22.py:
# Using names.txt containing over five-thousand first names, begin by sorting
# it into alphabetical order. Then working out the alphabetical value for each
# name, multiply this value by its alphabetical position in the list to obtain
# a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

# All letters
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# values of letters
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

# Read in the data
total_count = 0
names = []
with open('p022_names.txt') as f:
    names = sorted(f.read().replace('"', '').split(','), key=str)

for i, name in enumerate(names):
    count = 0
    for letter in name:
        for k, val_letter in enumerate(letters):
            if letter == val_letter:
                count += numbers[k]
    total_count += (i+1) * count

print("The value of all names is: " + str(total_count))
