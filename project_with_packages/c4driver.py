from connect4.c4engine import Engine

# This program is a connect 4 game

# @author: Kristian Trevino
# @version: 3/24/16 


import sys
import pickle

def main():

    e = Engine()
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
    currentGame = e.resetBoard(num_columns, num_rows)
    e.printBoard(currentGame, num_columns, num_rows)
    print ""
    print "You need",winLength,"in a row to WIN."
    print ""

    #file name for pickle
    loadFile = "loader"

#prompts user to start new game,load previous, or quit
    try:
        index = -1
        while index < 0:
            userInput =  e.gameLoader()
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
                e.printBoard(currentGame, num_columns, num_rows)
                move = e.playerInput(currentGame,player, num_columns,loadFile)
                e.placeToken(num_rows, currentGame, playerOne, move)
                if e.checkWinner(currentGame, playerOne, num_columns, num_rows):
                    winner = 'one'
                    break
                player = 'two'
            else:
                print ""
                e.printBoard(currentGame, num_columns, num_rows)
                move = e.playerInput(currentGame, player, num_columns,loadFile)
                e.placeToken(num_rows, currentGame, playerTwo, move)
                if e.checkWinner(currentGame, playerTwo, num_columns, num_rows):
                    winner = 'two'
                    break
                player = 'one'

            if e.isBoardFull(currentGame, num_columns, num_rows):
                winner = 'tie'
                break

        #prints out winner
        print ""
        e.printBoard(currentGame, num_columns, num_rows)
        print ""
        print('Player %s WINS!' % winner)
        print ""
        sys.exit()

if __name__ == '__main__':
    main()

