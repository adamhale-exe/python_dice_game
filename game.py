#dice game
import random
#roll a random number from 1-6 function
def roll():
    return random.randint(1,6)

#choose number of players (2-4)
def player_count():
    while True:
        number_of_players = input("Choose the number of players (2 - 4): ")
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

for i in range(len(total_score)):
    round_score = 0
    print("Ready Player", i + 1,"\nYour total score is", total_score[i])
    while True:
        play_choice = input("Would you like to roll? (y/n) ")
        if play_choice != "y":
            print("Your turn is over. You scored", round_score,"points")
            break
        current_roll = roll()
        print("You rolled a ",current_roll)
        #if dice rolls 1, 0 score and next person
        if current_roll == 1:
            round_score = 0
            print("Your turn is over. You scored", round_score,"points")
            break
        #else increment score by value
        round_score += current_roll
        print("Your score this round is", round_score)
    #update total score once round loop finished
    total_score[i] += round_score

#check after all players have had turn if anyone is over 50 score
#highest score wins