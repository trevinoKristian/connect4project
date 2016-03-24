# This program is a connect 4 game

# @author: Kristian Trevino
# @version: 3/24/16 


import sys
import pickle 

def main():

    #stores comand-line arguments in a list
    argList = sys.argv

    #sets command-line arguments to variables
    try:
        num_columns = int (argList[1])
        num_rows = int (argList[2])
        winLength = int(argList[3])
    except:
	print ""
	print " ERROR: Invalid command-line argumets"
	print ""
	sys.exit()
    
    #Welcome screen to new game
    print ""
    print "WELCOME TO CONNECT 4! "
    print ""
    print "A session has created with a", num_columns, "x", num_rows,"board." 
    print ""
    currentGame = resetBoard(num_columns, num_rows)
    printBoard(currentGame, num_columns, num_rows)
    print ""
    print "You need",winLength,"in a row to WIN."
    print ""

    #file name for pickle
    loadFile = "loader"

    #prompts user to start new game,load previous, or quit
    try:
        index = -1
        while index < 0:
            userInput =  gameLoader()
	    if userInput == 'n':
	        break
	    #loads previous saved game
	    if userInput == 'l':
	        print ""
	        print "Loading game ...."
	        f = open(loadFile, 'r')
	        try:
		    currentGame = pickle.load(f)
	        except pickle.UnpicklingError:
		    print ""
		    print "Unpickling Error, New Game started"
	        except EOFError:
		    print ""
		    print "End Of File Error, New Game started"
		
	        break
	    if userInput == 'q':
	        sys.exit()
	    else:
	        print ""
		print "Invalid entry. Please Try Again."
		print ""
    except:
	print ""
	print "An ERROR has occured."
	print ""    
	sys.exit()
      
    # allows players to input tokens and checks for winners
    while True:
       
        playerOne = 'X'
	playerTwo = 'O'
        
	player = 'one' 

        while True:
            if player == 'one':
		print ""
                printBoard(currentGame, num_columns, num_rows) 
                move = playerInput(currentGame,player, num_columns,loadFile)
                placeToken(num_rows, currentGame, playerOne, move)
                if checkWinner(currentGame, playerOne, num_columns, num_rows):
                    winner = 'one'
                    break
                player = 'two'
            else:
		print ""
		printBoard(currentGame, num_columns, num_rows)
		move = playerInput(currentGame, player, num_columns,loadFile)
                placeToken(num_rows, currentGame, playerTwo, move)
                if checkWinner(currentGame, playerTwo, num_columns, num_rows):
                    winner = 'two'
                    break
                player = 'one'

            if isBoardFull(currentGame, num_columns, num_rows):
                winner = 'tie'
                break

        #prints out winner
	print ""
	printBoard(currentGame, num_columns, num_rows)
	print ""
        print('Player %s WINS!' % winner)
	print ""
	sys.exit()

#CODE OUTSIDE OF MAIN
#(needs to be put into packages)

#resets the Connect4 game board and makes all values -1
def resetBoard(num_columns, num_rows):
    board = []

    for col in range(num_columns):
        board.append([])
        for row in range(num_rows):
            board[-1].append('.')
    return board

#prints out Connect4 game board
def printBoard(b, num_columns, num_rows):
    print('  '.join(map(lambda x: str(x + 1), range(num_columns))))
    for y in range(num_rows):
        print('  '.join(b[x][y] for x in range(num_columns)))

#prompts user to start new game or load from previous
def gameLoader():
    print('( n - new game, l - load, q - quit )\nWould you like to start a new game, load from previous session, or quit?')
    response = raw_input()
    return response

#takes in the player's input
def playerInput(board, player, num_columns,loadFile):
    while True:
	print ""
	print '( 1-%s | s - save & quit | e - exit )' % num_columns
        print "PLAYER %s: In which column would you like to place a token?" % player.upper()
        move = raw_input()
        if move == 'e':
            sys.exit()
	#saves game
	if move == 's':
	    print ""
	    print "*Game Saved*"
	    print ""
	    f = open(loadFile, 'wb')
	    try: 
		pickle.dump(board, f)
	    except pickle.PickleError:
		print "Pickle Error"
	    except pickle.PicklingError:
		print "Error found while pickling"
	    f.close()
	    sys.exit()
        if not move.isdigit():
            continue
        move = int(move) - 1
        if isValidMove(board, move, num_columns):
            return move
	else:
	    print ""
	    print " Invalid Entry. Please Try Again."

#places player's token on the board
def placeToken(num_rows, board, player, column):
    for y in range(num_rows-1, -1, -1):
        if board[column][y] == '.':  
            board[column][y] = player
            return

#determines whether move is valid
def isValidMove(board, move, num_columns):
    if move < 0 or move >= (num_columns):
        return False

    if board[move][0] != '.': 
        return False

    return True

#checks whether board is full
def isBoardFull(board, num_columns, num_rows):
    for x in range(num_columns):
        for y in range(num_rows):
            if board[x][y] == '.':  
                return False
    return True

#checks for winner
def checkWinner(board, player, num_columns, num_rows):

    # checks for horizontal winner
    for y in range(num_rows):
        for x in range(num_columns - 3):
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                return True

    # checks for vertical winner
    for x in range(num_columns):
        for y in range(num_rows - 3):
            if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                return True

    # checks for forward diagonal
    for x in range(num_columns - 3):
        for y in range(3, num_rows):
            if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                return True

    # checks for backward diagonal
    for x in range(num_columns - 3):
        for y in range(num_rows - 3):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                return True

    return False


if __name__ == '__main__':
    main()

