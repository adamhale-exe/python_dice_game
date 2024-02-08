#dice game
import random
#roll a random number from 1-6 function
def roll():
    return random.randint(1,6)
   
print(roll())
#choose number of players (2-4)
#create array of player scores based on number of players
#if dice rolls 1, 0 score and next person
#else increment score by value
#update total score if player chooses not to continue
#check after all players have had turn if anyone is over 50 score
#highest score wins