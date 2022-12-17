#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 54.py:


from enum import Enum
from collections import defaultdict


# Assign values to each hand, higher is better.
class Hands(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


# Transform special cards to a normal value.
def transform_hand(hand):
    for idx, i in enumerate(hand):
        if i == 'T': hand[idx] = 10
        elif i == 'J': hand[idx] = 11
        elif i == 'Q': hand[idx] = 12
        elif i == 'K': hand[idx] = 13
        elif i == 'A': hand[idx] = 14
        else: hand[idx] = int(i)

    return hand


# Find any duplicates in a list.
def find_duplicates(hand, t):
    card_dict = defaultdict(int)
    for i in hand:
        card_dict[i] += 1

    return [v for v in card_dict if card_dict[v] > t]


# Returns two values, the rank of the hand and the rank of the
# highest card if there is no clear winner.
def determine_hand(hand):
    # Separate lists for the suits and values.
    lst = [list(x)[0] for x in hand]
    suit = [list(x)[1] for x in hand]

    lst = transform_hand(lst)

    rank = []

    # Rank is highest card.
    if len(set(lst)) == len(lst):
        rank = [Hands.HIGH_CARD.value, max(lst)]

    # Rank is one pair.
    if len(set(lst)) == 4:
        # Determine the rank of the duplicates.
        pair = find_duplicates(lst, 1)
        mlst = [x for x in lst if x in pair]

        rank = [Hands.ONE_PAIR.value, max(mlst)]

    # Ranks for two pair and three of a kind. Same course of action
    # for one pair.
    if len(set(lst)) == 3:
        # Two pair.
        if len(find_duplicates(lst, 1)) == 2:
            pair = find_duplicates(lst, 1)
            mlst = [x for x in lst if x in pair]

            rank = [Hands.TWO_PAIR.value, max(mlst)]
        # Three of a kind.
        else:
            pair = find_duplicates(lst, 2)
            mlst = [x for x in lst if x in pair]
            rank = [Hands.THREE_KIND.value, max(mlst)]

    # Rank is straight.
    if sorted(lst) == list(range(min(lst), min(lst) + 5)):
        rank = [Hands.STRAIGHT.value, 0]

    # Rank is flush or straight flush.
    if len(set(suit)) == 1:
        # Check for consecutive numbers.
        if sorted(lst) == list(range(min(lst), min(lst) + 5)):
            rank = [Hands.STRAIGHT_FLUSH, max(lst)]
        else:
            rank = [Hands.FLUSH.value, max(lst)]

    # Ranks for full house or four of a kind.
    if len(set(lst)) == 2:
        if len(find_duplicates(lst, 3)):
            pair = find_duplicates(lst, 3)
            mlst = [x for x in lst if x in pair]
            rank = [Hands.FOUR_KIND.value, max(mlst)]
        else:
            rank = [Hands.FULL_HOUSE.value, max(lst)]

    # Rank for royal flush.
    if len(set(suit)) == 1 and 10 in lst and 11 in lst and 12 in lst and 13 in lst and 14 in lst:
        rank = [Hands.ROYAL_FLUSH.value, max(lst)]

    return rank


player_1_wins = 0

with open('poker.txt', 'r') as f:
    for line in f:
        # Clean lines.
        line = line.strip().split(' ')

        # The hands for each players.
        player1 = line[:5]
        player2 = line[5:]

        # Check how good the hand is.
        rank_1 = determine_hand(player1)
        rank_2 = determine_hand(player2)

        # Check which hand is greater or if highest card is greater.
        if rank_1[0] > rank_2[0] or (rank_1[0] == rank_2[0] and rank_1[1] > rank_2[1]):
            player_1_wins += 1

print("Amount of wins for player 1:", player_1_wins)

