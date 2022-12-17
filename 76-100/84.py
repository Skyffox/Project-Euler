#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 84.py:

import random

def die_rolls():
    die1 = random.randint(1, 4)
    die2 = random.randint(1, 4)

    return die1, die2

board = {"GO" : 0, "A1" : 0, "CC1" : 0, "A2" : 0, "T1" : 0, "R1" : 0, "B1" : 0,
      "CH1" : 0, "B2" : 0, "B3" : 0, "JAIL" : 0, "C1" : 0, "U1" : 0, "C2" : 0,
      "C3" : 0, "R2" : 0, "D1" : 0, "CC2" : 0, "D2" : 0, "D3" : 0, "FP" : 0,
      "E1" : 0, "CH2" : 0, "E2" : 0, "E3" : 0, "R3" : 0, "F1" : 0, "F2" : 0,
      "U2" : 0, "F3" : 0, "G2J" : 0, "G1" : 0, "G2" : 0, "CC3" : 0, "G3" : 0,
      "R4" : 0, "CH3" : 0, "H1" : 0, "T2" : 0, "H2" : 0}


chance_cards = list(range(1, 17))
community_chest = list(range(1, 17))
random.shuffle(chance_cards)
random.shuffle(community_chest)

num_rolls = 0
player_pos = 0
consecutive_doubles = 0

while num_rolls < 1000000:
    num_rolls += 1
    roll = die_rolls()

    if roll[0] == roll[1]:
        consecutive_doubles += 1
        if consecutive_doubles > 2:
            consecutive_doubles = 0
            player_pos = 10 # jail position on board
            continue
    else:
        consecutive_doubles = 0

    player_pos = (player_pos + sum(roll)) % len(board)

    if player_pos == 7 or player_pos == 22 or player_pos == 36:
        z = community_chest[0]
        community_chest.pop(0)
        community_chest.append(z)
        if z == 1:
            player_pos = 0 # go position on board
        elif z == 2:
            player_pos = 10 # jail position on board

    if player_pos == 2 or player_pos == 17 or player_pos == 33:
        z = chance_cards[0]
        chance_cards.pop(0)
        chance_cards.append(z)
        if z == 1:
            player_pos = 0 # go position on board
        elif z == 2:
            player_pos = 10 # jail position on board
        elif z == 3:
            player_pos = 11 # C1 position on board
        elif z == 4:
            player_pos = 24 # E3 position on board
        elif z == 5:
            player_pos = 39 # H2 position on board
        elif z == 6:
            player_pos = 5 # R1 position on board
        elif z == 7 or z == 8:
            # go to next r 5 15 25 35 R positions
            if player_pos == 7:
                player_pos = 15
            elif player_pos == 22:
                player_pos = 25
            elif player_pos == 36:
                player_pos = 5
        elif z == 9:
            # go to next u 22 is CC pos and 28 and 12 are U pos
            if player_pos == 22:
                player_pos = 28
            else:
                player_pos = 12
        elif z == 10:
            # go back 3 squares
            player_pos -= 3

    if player_pos == 30:
        player_pos = 10 # jail position on board

    x = list(board)[player_pos]
    board[x] += 1

top_3 = sorted(board, key=board.get, reverse=True) #[0:3]
for i, k in enumerate(board):
    if k == top_3[0]:
        string1 = str(i)
        if i < 10:
            string1 = "0" + string1
    if k == top_3[1]:
        string2 = str(i)
        if i < 10:
            string2 = "0" + string2
    if k == top_3[2]:
        string3 = str(i)
        if i < 10:
            string3 = "0" + string3

six_digit_modal_string = string1 + string2 + string3

print(top_3)
print(six_digit_modal_string)
print(board)
