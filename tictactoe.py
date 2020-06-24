row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['X', 'X', 'X']
board = [row1, row2, row3]


def display(brd):
    print(brd[0])
    print(brd[1])
    print(brd[2])


def player_input():
    positionX = int(input('enter the x value'))
    positionY = int(input('enter the Y value'))
    return positionX, positionY


# X, Y = player_input()
# print(X, Y)


def place_marker(brd, x, y):
    brd[x][y] = 'X'
    return brd


# board = place_marker(board, X, Y)
# display(board)


# takes in a board and a mark (X or O) and then checks to see if the mark has won
def win_check(brd, mark):
    verCheck = False
    winrow = [mark, mark, mark]
    for row in brd:
        if row == winrow:
            return True
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if i == j:
                if brd[i][j] == mark:
                    priD = True
                else:
                    priD = False
        if i + j == 2:
            if brd[i][j] == mark:
                secD = True
            elif brd[i][j] != mark:
                secD = False
    for r1, r2, r3 in brd:
        for i in range(3):
            if r1[i] == mark and r2[i] == mark and r3[i] == mark:
                verCheck = True
            elif not verCheck:
                verCheck = False

    if priD == True or secD == True or verCheck == True:
        return True
    else:
        return False


if win_check(board, 'X'):
    print('Win')
else:
    print('Lose')

# randomly decides which player goes first
def choose_first():
    pass


# returns a boolean indicating whether a space on the board is freely available
def space_check(board):
    pass


# checks if the board is full and returns a boolean value. True if full,False otherwise
def full_board_check(board):
    pass


# asks for a player's next position and then uses the space_check function to check is it's a free position. If it
# is, then return the position for later use.
def player_choice(board):
    pass


# returns a boolean True if they do want to play again
def replay():
    pass

# print('Welcome to Tic Tac Toe!')

# while True:
# Set the game up here
# pass

# while game_on:
# Player 1 Turn


# Player2's turn.

# pass

# if not replay():
# break