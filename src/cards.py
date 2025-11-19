# cards.py

import yaml

class ActionCard:
    def __init__(self, name, card_type, effects, point_values):
        self.name = name
        self.card_type = card_type
        self.effects = effects
        self.point_values = point_values

    def apply_effect(self, player):
        # Apply effects to player
        for effect in self.effects:
            if effect['type'] == 'points':
                player.update_scores(self.point_values[effect['category']])
        return player

class SituationCard:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def resolve(self, game_state):
        # Resolve the effects of the situation card on the game state
        for effect in self.effects:
            if effect['type'] == 'penalty':
                game_state['players'][effect['player_index']].update_scores(-effect['value'])
        return game_state

# Load action cards from a YAML file
def load_action_cards(file_path):
    with open(file_path, 'r') as file:
        action_cards_data = yaml.safe_load(file)
        return [ActionCard(**card) for card in action_cards_data]

# Load situation cards from a YAML file
def load_situation_cards(file_path):
    with open(file_path, 'r') as file:
        situation_cards_data = yaml.safe_load(file)
        return [SituationCard(**card) for card in situation_cards_data]

