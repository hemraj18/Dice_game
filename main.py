import random

# Set a Dice roll 
def roll():
    return random.randint(1, 6)

# Take the Number of players 
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)    
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4") 
    else:
        print("Invalid, Try again")

# Maximum score to win the Game
max_score = 50   
# To store the scores of the players in the list
player_score = [0 for _ in range(players)]
player_names = []

# Get player names
for player_id in range(players):
    player_name = input(f"Enter the name of player {player_id + 1}: ")
    player_names.append(player_name)

# Actual game starts here
while max(player_score) < max_score:
    for player_id in range(players):  
        # Need a Blank space in between 
        print(" ") 
        message = f" It's {player_names[player_id]}'s Turn"
        #to center the print statement
        print(message.center(40, '*'))                  
        print(f"Your total score is {player_score[player_id]}")
        to_win = max_score - player_score[player_id]
        print(f"To win, you need {to_win}")
        # Initialize the current score
        current_score = 0

        # Ask the player to Start the game or continue the game or to quit
        while True:
            should_roll = input("\nDo you want to play? (Enter 'y'): ")
            if should_roll.lower() != 'y':
                break
            
            value = roll()

            if value == 1:
                print("You rolled 1, turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")

            print(f"Current score is {current_score}")
            # Check how much the player needs to win the game 
            if player_score[player_id] != 0:
                done = to_win - current_score
                if done <= 0:
                    break 
                else:
                    print(f"Now you need {done}")
            else:
                done = max_score - current_score
                if done <= 0:
                    break 
                else:
                    print(f"Now you need {done}")

        # Add the current score to the total score
        player_score[player_id] += current_score
        print(f"Your total score is {player_score[player_id]}")    

# Finally displaying the winner
max_score = max(player_score)
winner_index = player_score.index(max_score)
winner_name = player_names[winner_index]
print(f"\nWinner is {winner_name} with a score of {max_score}")
