# pylint: disable=line-too-long
"""
Problem 54: Poker Hands

Problem description:
This problem involves simulating a poker game to determine how many hands Player 1 wins. 
Each line of the file contains two poker hands, one for Player 1 and the other for Player 2. 
Each hand contains five cards, and the goal is to compare the hands and determine the winner 
based on the rank of the hand. The hands are evaluated using standard poker hand rankings, 
from High Card to Royal Flush.

The objective is to calculate how many hands Player 1 wins over all the hands in the file.

Poker hand rankings (from worst to best):
- High Card
- One Pair
- Two Pair
- Three of a Kind
- Straight
- Flush
- Full House
- Four of a Kind
- Straight Flush
- Royal Flush

Answer: 376
"""

from enum import Enum
from collections import defaultdict
from typing import List
from utils import profiler


class Hands(Enum):
    """Assign values to each hand, higher is better."""
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


def transform_hand(hand: List[str]) -> List[int]:
    """
    Transforms special cards (T, J, Q, K, A) into their corresponding numeric values.
    
    Args:
        hand (list): A list of cards represented as strings.
    
    Returns:
        list: A list of numeric values representing the cards.
    """
    for idx, i in enumerate(hand):
        if i == 'T':
            hand[idx] = 10
        elif i == 'J':
            hand[idx] = 11
        elif i == 'Q':
            hand[idx] = 12
        elif i == 'K':
            hand[idx] = 13
        elif i == 'A':
            hand[idx] = 14
        else:
            hand[idx] = int(i)

    return hand


def find_duplicates(hand: List[int], t: int) -> List[int]:
    """
    Finds any duplicates in a list of cards (cards that appear more than 't' times).
    
    Args:
        hand (list): A list of card values.
        t (int): The threshold for duplicates. The function returns values that appear more than 't' times.
    
    Returns:
        list: A list of duplicate values in the hand.
    """
    card_dict = defaultdict(int)
    for i in hand:
        card_dict[i] += 1

    return [v for v in card_dict if card_dict[v] > t]


def determine_hand(hand: List[int]) -> List[int]:
    """
    Determines the rank of a given hand in poker and returns a tuple containing the rank and the highest card (if applicable).
    
    Args:
        hand (list): A list of 5 cards.
    
    Returns:
        list: A list containing two values: the rank of the hand and the highest card if applicable.
    """
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
        pair = find_duplicates(lst, 1)
        mlst = [x for x in lst if x in pair]
        rank = [Hands.ONE_PAIR.value, max(mlst)]

    # Two pair or three of a kind
    if len(set(lst)) == 3:
        if len(find_duplicates(lst, 1)) == 2: # Two pair.
            pair = find_duplicates(lst, 1)
            mlst = [x for x in lst if x in pair]
            rank = [Hands.TWO_PAIR.value, max(mlst)]
        else: # Three of a kind.
            pair = find_duplicates(lst, 2)
            mlst = [x for x in lst if x in pair]
            rank = [Hands.THREE_KIND.value, max(mlst)]

    # Rank is straight.
    if sorted(lst) == list(range(min(lst), min(lst) + 5)):
        rank = [Hands.STRAIGHT.value, 0]

    # Rank is flush or straight flush.
    if len(set(suit)) == 1:
        if sorted(lst) == list(range(min(lst), min(lst) + 5)):
            rank = [Hands.STRAIGHT_FLUSH.value, max(lst)]
        else:
            rank = [Hands.FLUSH.value, max(lst)]

    # Full house or four of a kind.
    if len(set(lst)) == 2:
        if len(find_duplicates(lst, 3)):
            pair = find_duplicates(lst, 3)
            mlst = [x for x in lst if x in pair]
            rank = [Hands.FOUR_KIND.value, max(mlst)]
        else:
            rank = [Hands.FULL_HOUSE.value, max(lst)]

    # Royal flush.
    if len(set(suit)) == 1 and 10 in lst and 11 in lst and 12 in lst and 13 in lst and 14 in lst:
        rank = [Hands.ROYAL_FLUSH.value, max(lst)]

    return rank


@profiler
def compute() -> int:
    """
    Reads the input file, evaluates all the poker hands, and counts how many times Player 1 wins.
    
    Returns:
        int: The number of hands Player 1 wins.
    """
    player_1_wins = 0
    with open('inputs/poker.txt', 'r', encoding="utf-8") as f:
        for line in f:
            # Clean lines.
            line = line.strip().split(' ')

            # The hands for each player.
            player1 = line[:5]
            player2 = line[5:]

            # Check how good the hand is.
            rank_1 = determine_hand(player1)
            rank_2 = determine_hand(player2)

            # Check which hand is better.
            if rank_1[0] > rank_2[0] or (rank_1[0] == rank_2[0] and rank_1[1] > rank_2[1]):
                player_1_wins += 1

    return player_1_wins


if __name__ == "__main__":
    print(f"Problem 54: {compute()}")
