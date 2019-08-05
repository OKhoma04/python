# User will be X by default, O is a computer move
# In the end of the game there is no special message (like: do you want to try one more time?)
# Case when no one won has been implemented.
# Used random for the computer moves
# Verification of cell ocupation and type of symbol has been implemented

# use random build in function
import random

# set range for gameboard as list
gameboard = [x for x in range(1,10)]
print('First move will be player X')        # User will be X by default, O is a computer move

# create function board(). Purpose is to use for every iteration
def board():
    print ("-------------")
    for i in range(3):
        print( "|", gameboard[0+i*3], "|", gameboard[1+i*3], "|", gameboard[2+i*3], "|")
        print("-------------")
board()

# Populate letter X or O in gameboard list
def insertLetter(letter, pos):
    gameboard[pos] = letter

# Win combinations
def isWinner(bo, le):
# Given a board and a player’s letter, this function returns True if that player has won.
 return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the top
         (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
         (bo[0] == le and bo[1] == le and bo[2] == le) or # across the bottom
         (bo[6] == le and bo[3] == le and bo[0] == le) or # down the left side
         (bo[7] == le and bo[4] == le and bo[1] == le) or # down the middle
         (bo[8] == le and bo[5] == le and bo[2] == le) or # down the right side
         (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
         (bo[8] == le and bo[4] == le and bo[0] == le)) # diagonal

# Verify possible moves. Exclude X and O from possible moves
possible_move = [x for x in gameboard if x != 'X' and x != 'O']

# Execute code while someone wins
for let in ['X', 'O']:
    while not isWinner(gameboard, let):
            try:
                move = int(input('Pick a number from 1-9:'))                # Show message, pick a number
                if move in possible_move:                                   # If your move is right then at first time move as X, rewrite gameboard with new values
                    insertLetter('X', move-1)
                    if isWinner(gameboard, 'X'):                            # Verify does X is winner, exit from loop
                        print('X, won the game!')
                        break
                    if gameboard.count('X') == 5:                           # Raise message when no one win
                        print('Game over, no one win!')
                        break

                    possible_move = [x for x in gameboard if x != 'X' and x != 'O']     #Exclude X and O from possible moves
                    move_PC = random.choice(possible_move)                  # Select random move for PC
                    insertLetter('O',move_PC-1)                             # Isert O on this position
                    if isWinner(gameboard, 'O'):                            # Verify does O is winner, exit from loop
                        print('O, won the game!')
                        break
                    possible_move = [x for x in gameboard if x != 'X' and x != 'O']     #Exclude X and O from possible moves
                    board()

                else:
                    print('Sorry, this cell is occupied!')                 # Raise message when cell is not free
            except:
                print('Please type a number!')                             # Raise message when inserted symbol is not a number
    break
board()

