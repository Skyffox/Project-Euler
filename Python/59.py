# Decrypt the message and find the sum of the ASCII values in the original text.
# Execution time: 5.585s

# Create list of valid characters in the text.
# Add capital and normal letters and numbers.
valid = list(range(65, 91)) + list(range(48, 58)) + list(range(97, 123))

# Add some specials characters.
valid += [32, 33, 39, 40, 41, 44, 46, 59]

# Make them ascii characters.
c_valid = [chr(x) for x in valid]

# Open the encrypted file with ascii characters.
with open("inputs/p059_cipher.txt", "r") as f:
    vals = f.read().strip().split(',')
    vals = [int(x) for x in vals]


valid_txts = []

# Try every key possible.
for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            txt = []
            b = False

            # Run the key over the file.
            for l in range(0, len(vals), 3):
                # Try catch to work with wrap-around.
                try:
                    txt.append(chr(vals[l] ^ i))
                    txt.append(chr(vals[l+1] ^ j))
                    txt.append(chr(vals[l+2] ^ k))
                except:
                    pass

            for char in txt:
                if char not in c_valid:
                    b = True
                    break

            # Create a list of valid texts.
            if not b:
                valid_txts.append(txt)

s = 0

for text in valid_txts:
    print(''.join(text))
    for letter in text:
        s += ord(letter)

print ("sum of decrypted ascii values:", s)
