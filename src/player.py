# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = {'E': 0, 'P': 0}
        self.hand = []

    def update_scores(self, points):
        # Update the player's scores based on actions taken
        self.scores['E'] += points.get('E', 0)
        self.scores['P'] += points.get('P', 0)
        return self.scores

    def draw_hand(self, cards, number):
        # Draw a specified number of cards into the player's hand
        self.hand.extend(cards[:number])
        return self.hand

    def select_card(self, cards):
        # Logic to select a card from hand (to be implemented)
        pass

    def has_won(self):
        # Check if the player has met the win conditions
        return False  # Placeholder logic

