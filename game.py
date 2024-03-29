#dice game
import random
import time
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

print(r"""
  ____                    _ _ 
 /\' .\    _____       __| (_) ___ ___     __ _  __ _ _ __ ___   ___ 
/: \___\  / .  /\     / _` | |/ __/ _ \   / _` |/ _` | '_ ` _ \ / _ \
\' / . / /____/..\   | (_| | | (_|  __/  | (_| | (_| | | | | | |  __/
 \/___/  \'  '\  /    \__,_|_|\___\___|   \__, |\__,_|_| |_| |_|\___|
          \'__'\/                         |___/
      """)
print("\nInstructions:\nThis is a simple addition game of risk and reward.\nKeep rolling a single die to improve your score.\nBut get too greedy, roll a 1, and lose all your points for that turn.\nFirst to 30 wins!\n")
players = player_count()

#create list of player scores based on number of players
total_score = [0 for _ in range(players)]

#check after all players have had turn if anyone is over 50 score
while max(total_score) < 30:
    for i in range(len(total_score)):
        round_score = 0
        print("------------------------\n---- Ready Player", i + 1,"----\n------------------------\n-> Your total score is", total_score[i])
        while True:
            play_choice = input("Would you like to roll? (y/n) ")
            if play_choice != "y":
                print("Your turn is over. You scored", round_score,"points")
                break
            current_roll = roll()
            print("\nYou rolled a",current_roll,"\n")
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
        print("Your new total score is", total_score[i])

#highest score wins
winner_index = total_score.index(max(total_score))
print("\n.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.\n\nPlayer", winner_index + 1, "wins with a score of", max(total_score),"\n\n.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.")

#sleep for 10 seconds before application closes
print("\nThe game will close in 10 seconds")
time.sleep(10)