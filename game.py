#dice game
import random
#roll a random number from 1-6 function
def roll():
    return random.randint(1,6)

#choose number of players (2-4)
def player_count():
    while True:
        number_of_players = input("Choose the number of players (2 - 4):")
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
            if 2 <= number_of_players <= 4:
                break
            print("Error: Number of players needs to be between 2 and 4")
        else:
            print("Error: Number of players must be a digit")
    return number_of_players

players = player_count()

#create list of player scores based on number of players
total_score = [0 for _ in range(players)]
print(total_score)

#if dice rolls 1, 0 score and next person
#else increment score by value
#update total score if player chooses not to continue
#check after all players have had turn if anyone is over 50 score
#highest score wins