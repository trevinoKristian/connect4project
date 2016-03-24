class Engine:

    #resets the Connect4 game board and makes all values -1
    def resetBoard(self,num_columns, num_rows):
        board = []

        for col in range(num_columns):
            board.append([])
            for row in range(num_rows):
                board[-1].append('.')
        return board

    #prints out Connect4 game board
    def printBoard(self,b, num_columns, num_rows):
        print('  '.join(map(lambda x: str(x + 1), range(num_columns))))
        for y in range(num_rows):
            print('  '.join(b[x][y] for x in range(num_columns)))

    #prompts user to start new game or load from previous
    def gameLoader(self):
        print('( n - new game, l - load, q - quit )\nWould you like to start a new game, load from previous session, or quit?')
        response = raw_input()
        return response

    #determines whether move is valid
    def isValidMove(self,board, move, num_columns):
        if move < 0 or move >= (num_columns):
            return False

        if board[move][0] != '.':
            return False

        return True

    #takes in the player's input
    def playerInput(self,board, player, num_columns,loadFile):
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
    def placeToken(self,num_rows, board, player, column):
        for y in range(num_rows-1, -1, -1):
            if board[column][y] == '.':
                board[column][y] = player
                return

    #checks whether board is full
    def isBoardFull(self,board, num_columns, num_rows):
        for x in range(num_columns):
            for y in range(num_rows):
                if board[x][y] == '.':
                    return False
        return True

    #checks for winner
    def checkWinner(self,board, player, num_columns, num_rows):

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


