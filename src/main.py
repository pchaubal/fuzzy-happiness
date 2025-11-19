# main.py

# Import necessary modules
import game
import player
import cards

# Function to start the game
def start_game():
    # Initialize game state
    game_state = game.initialize_game()  # Assuming there's an initialize_game method in game.py
    print("Game started!\n")

    while not game.check_win_condition():
        for current_player in game_state['players']:
            # Draw cards
            action_cards = game.draw_cards(current_player)
            situation_card = game.draw_situation_card()
            print(f"Player {current_player.name} drew {len(action_cards)} action cards and a situation card.")

            # Player plays cards
            for _ in range(3):  # Allow the player to play up to 3 cards
                card_to_play = current_player.select_card(action_cards)  # Assuming there's a method for selecting a card
                if card_to_play:
                    game.play_card(current_player, card_to_play)
                    print(f"Player {current_player.name} played {card_to_play.name}.")
            
            current_player.update_scores()
            # Check for win condition after player's turn
            if game.check_win_condition():
                break

    # End game
    end_game(game_state)

# Function to end the game
def end_game(game_state):
    winner = game_state['winner']
    print(f"Game over! The winner is {winner.name} with {winner.scores} points.")

if __name__ == "__main__":
    start_game()

