import random

row1 = ['O', '-', ' ']
row2 = ['O', '-', 'X']
row3 = ['O', '-', 'X']
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
    priD = False
    secD = False
    priDiagonalList = []
    secDiagonalList = []
    columns = [['', '', ''], ['', '', ''], ['', '', '']]
    winrow = [mark, mark, mark]
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            columns[i][j] = brd[j][i]
            if i == j:
                priDiagonalList.append(brd[i][j])
            if i + j == 2:
                secDiagonalList.append(brd[i][j])
    if priDiagonalList == winrow:
        priD = True
    if secDiagonalList == winrow:
        secD = True
    for row in brd:
        if row == winrow:
            return True
    for col in columns:
        if col == winrow:
            return True

    if priD == True or secD == True or verCheck == True:
        return True
    else:
        return False


# if win_check(board, 'X'):
#     print('Win')
# else:
#     print('Lose')


# randomly decides which player goes first
def choose_first():
    return random.randint(1, 2)


# print(choose_first())


# checks if the board is full and returns a boolean value. True if full,False otherwise
def full_board_check(brd):
    for r1, r2, r3 in brd:
        if ' ' in r1 or ' ' in r2 or ' ' in r3:
            return False
        else:
            return True


# if full_board_check(board):
#     print('Board is full')
# else:
#     print('Empty spaces are available')

# returns a boolean indicating whether a space on the board is freely available
def space_check(brd,x,y):
    if not full_board_check(brd):
        if brd[x][y] == ' ':
            return True
        else:
            return False

# print(space_check(board,1,2))

# asks for a player's next position and then uses the space_check function to check is it's a free position. If it
# is, then return the position for later use.
def player_choice(board):
    pass


# returns a boolean True if they do want to play again
def replay():
    ans = input('Would you like to play again? Type yes or no ')
    print(ans)
    if ans == 'yes':
        return True
    elif ans == 'no':
        return False
    else:
        replay()

# if replay():
#     print('yes')
# else:
#     print('no')

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
