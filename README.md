# Pig Dice Game

The Pig dice game is a simple two-player dice game where the players take turns rolling a single die. The goal of the game is to reach a certain score threshold before your opponent. Players accumulate points by rolling the die and can choose to hold their current points or continue rolling, risking losing all their points for that turn if they roll a 1.

## How to Play

1. **Setup**: Determine the first player randomly. Each player starts with a score of 0.

2. **Taking Turns**: On a player's turn, they roll a single six-sided die.

3. **Scoring**: 
   - If the player rolls a 1, they score no points for that turn and their turn ends.
   - If the player rolls a number other than 1, they add that number to their current turn total and may choose to continue rolling or hold their score.
   - If the player chooses to hold, their turn total is added to their overall score, and their turn ends.
   
4. **Winning the Game**: The first player to reach or exceed a predetermined score threshold (e.g., 100 points) wins the game.

## Implementation

This Pig dice game is implemented in Python and provides a simple text-based interface for players to interact with. The game includes features such as alternating player turns, scoring, and a win condition.

## Running the Game

To run the Pig dice game, ensure you have Python installed on your system. Clone this repository, navigate to the directory containing the game file and run with Python!

