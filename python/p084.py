# pylint: disable=line-too-long
"""
Problem 84: Monopoly Odds

Problem description:
This module simulates the movement of a player on a Monopoly board using two 4-sided dice. 
The simulation runs for 1,000,000 rolls, and tracks the frequency of each space visited on 
the board, applying the effects of Chance and Community Chest cards as well as the special 
rules for rolling doubles and going to Jail. The objective is to identify the three most 
frequently visited spaces after all the rolls.

After completing the simulation, the module returns the names of the three most visited spaces 
on the Monopoly board along with a six-digit string representing the indices of these spaces 
on the board.

Answer: 101524 (Getting this is a bit random)
"""

import random
from typing import Tuple
from utils import profiler


def die_rolls() -> Tuple[int, int]:
    """
    Simulates the rolling of two 4-sided dice.
    
    Returns:
        tuple: Two integers representing the results of the dice rolls.
    """
    die1 = random.randint(1, 4)
    die2 = random.randint(1, 4)
    return die1, die2


@profiler
def compute() -> str:
    """
    Simulates the movement of a player around a Monopoly board using two 4-sided dice.
    Tracks the player's position and applies the effects of Chance and Community Chest cards.
    After 1,000,000 rolls, the function identifies the three most visited spaces and returns
    their names and the corresponding six-digit modal string representing the indices of these spaces.

    Returns:
        A six-digit string formed by concatenating the indices of these spaces.
    """
    # Monopoly board positions (names as keys and visit counts as values)
    board = {
        "GO": 0, "A1": 0, "CC1": 0, "A2": 0, "T1": 0, "R1": 0, "B1": 0,
        "CH1": 0, "B2": 0, "B3": 0, "JAIL": 0, "C1": 0, "U1": 0, "C2": 0,
        "C3": 0, "R2": 0, "D1": 0, "CC2": 0, "D2": 0, "D3": 0, "FP": 0,
        "E1": 0, "CH2": 0, "E2": 0, "E3": 0, "R3": 0, "F1": 0, "F2": 0,
        "U2": 0, "F3": 0, "G2J": 0, "G1": 0, "G2": 0, "CC3": 0, "G3": 0,
        "R4": 0, "CH3": 0, "H1": 0, "T2": 0, "H2": 0
    }

    # Chance and Community Chest cards (simulated as numbers 1-16)
    chance_cards = list(range(1, 17))
    community_chest = list(range(1, 17))
    random.shuffle(chance_cards)
    random.shuffle(community_chest)

    # Variables for simulation
    player_pos = 0
    turns = 100000

    # Running the simulation for 1,000,000 rolls
    for _ in range(turns):
        # Update the board with the player's visit
        x = list(board)[player_pos]
        board[x] += 1

        roll = die_rolls()
        total = sum(roll)
        # Check for doubles
        if roll[0] == roll[1]: # Double check
            roll2 = die_rolls()
            if roll2[0] == roll2[1]:
                roll3 = die_rolls()
                if roll3[0] == roll3[1]:
                    player_pos = 10 # Jail
                    continue
                else:
                    total += sum(roll2) + sum(roll3)
            else:
                total += sum(roll2)

        # Move the player on the board
        player_pos = (player_pos + total) % len(board)

        # Apply Community Chest effects
        if player_pos == 2 or player_pos == 17 or player_pos == 33:
            z = community_chest.pop(0)
            community_chest.append(z)
            if z == 1:
                player_pos = 0 # Go to Go
            elif z == 2:
                player_pos = 10 # Go to Jail

        # Apply Chance Card effects
        if player_pos == 7 or player_pos == 22 or player_pos == 36:
            z = chance_cards.pop(0)
            chance_cards.append(z)
            if z == 1:
                player_pos = 0 # Go to Go
            elif z == 2:
                player_pos = 10 # Go to Jail
            elif z == 3:
                player_pos = 11 # C1
            elif z == 4:
                player_pos = 24 # E3
            elif z == 5:
                player_pos = 39 # H2
            elif z == 6:
                player_pos = 5 # R1
            elif z == 7 or z == 8: # Go to the next R positions
                if player_pos < 5 or player_pos >= 35:
                    player_pos = 5
                elif player_pos >= 5 and player_pos < 15:
                    player_pos = 15
                elif player_pos >= 15 and player_pos < 25:
                    player_pos = 25
                elif player_pos >= 25 and player_pos < 35:
                    player_pos = 35
            elif z == 9: # Go to next U position
                if player_pos < 12 or player_pos >= 28:
                    player_pos = 12
                else:
                    player_pos = 28
            elif z == 10: # Go back 3 spaces
                player_pos -= 3

        # If the player lands on Jail (position 30), they are sent to Jail
        if player_pos == 30:
            player_pos = 10 # Jail

    # Find the top 3 most visited spaces
    top_3 = sorted(board, key=board.get, reverse=True)[:3]

    # Create a six-digit modal string representing the indices of the top 3 spaces
    six_digit_modal_string = "".join([f"{list(board.keys()).index(key):02d}" for key in top_3])

    return six_digit_modal_string


if __name__ == "__main__":
    print(f"Problem 84: {compute()}")
