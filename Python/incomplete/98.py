
# By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. 
# What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962.
# What is the largest square number formed by any member of such a pair?
# Execution time: ???

f = open("p098_words.txt", "r")

for words in f:
    words = words.split(",")
    words = [eval(x) for x in words]


longest = max([len(i) for i in words])
lst = [[] for x in range(0, longest)]
[lst[len(i) - 1].append(i) for i in words]

pairs = []
for len_word in lst:
    for word in len_word:
        w1 = sorted(list(str(word)))
        for word2 in len_word:
            w2 = sorted(list(str(word2)))
            if w1 == w2 and word != word2:
                pairs.append((word, word2))

real_pairs = []
encountered = []
for pair in pairs:
    if pair[1] not in encountered:
        real_pairs.append(pair)
    encountered.append(pair[0])

word_orders = []
for pair in real_pairs:
    word_list1 = list(str(pair[0]))
    word_list2 = list(str(pair[1]))
    word_order = [0] * len(word_list1)

    for c1, letter in enumerate(word_list1):
        for c2, find in enumerate(word_list2):
            if letter == find:
                word_order[c1] = c2
                word_list2[c2] = "NA"
                break

    word_orders.append(word_order)

choices = []
for l in range(2, 10):
    largest_number = 1
    l1 = l - 1
    while l > 0:
        largest_number *= 9
        l -= 1

    low = int((10**l1)**0.5)
    high = int(largest_number**0.5)
    choices.append([i**2 for i in range(low, high) if i**2 > 10**l1])


best = 0
for order in word_orders:
    squares = choices[len(order) - 2]
    for s in squares:
        s2 = list(str(s))
        s2 = [int(i) for i in s2]
        num = []
        for o in order:
            num.append(s2[o])

        num2 = int("".join(map(str, num)))
        if num2 in squares and num2 != s:
            b = max(s, num2)
            if b > best:
                best = b

print(best)
