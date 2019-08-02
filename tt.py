# use random build in function
import random

# set range for gameboard as list
gameboard = [x for x in range(1,10)]

# create function board(). Purpose is to use every iteration
def board():
    print ("-------------")
    for i in range(3):
        print( "|", gameboard[0+i*3], "|", gameboard[1+i*3], "|", gameboard[2+i*3], "|")
        print("-------------")
board()

# Populate letter X or O in gameboard list
def insertLetter(letter, pos):
    gameboard[pos] = letter

def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = [(1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9),
                   (1, 4, 7),
                   (2, 5, 8),
                   (3, 6, 9),
                   (1, 5, 9),
                   (3, 5, 7)]


# Verify possible moves. Exclude X and O from possible moves
possible_move = [x for x in gameboard if x != 'X' and x != 'O']

print(gameboard)
#def playerMove():

#run = True
#while run:
while not winner(gameboard):
    try:
        move = int(input('Pick a number from 1-9:'))                    # Show message
        if move in possible_move: #move > 0 and move < 10:              # If your move is right then at first time move as X
                insertLetter('X', move-1)
                possible_move = [x for x in gameboard if x != 'X' and x != 'O']     #Exclude X and O from possible moves
                move_PC = random.choice(possible_move)                  # Select random move for PC
                insertLetter('O',move_PC-1)                             # Isert O on this position
                possible_move = [x for x in gameboard if x != 'X' and x != 'O']     #Exclude X and O from possible moves
                print(gameboard)
                print(possible_move)
                print(move_PC)
                board()
                for a, b, c in WIN_COMBINATIONS:
                    if gameboard[a] == gameboard[b] == gameboard[c]:
                        print('Hooray! You have won the game!')
                    #gameIsPlaying = False
               # else:
                    #if isBoardFull(theBoard):
                        #drawBoard(theBoard)
                        #print('The game is a tie!')
                       # break
            #if spaceIsFree(move):
                #run = False
                #insertLetter('X', move-1)
                #board()

            #else:
                #print('Sorry, this space is occupied!')
        #else:
            #print('Pick a number from 1-9:')
            #board()
        else:
                print('Sorry, this space is occupied!')
    except:
        print('Please type a number!')
        board()

board()

