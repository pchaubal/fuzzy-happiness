# utils.py

import random

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def random_selection(cards):
    return random.choice(cards)  # Selects a random card from the provided list.

