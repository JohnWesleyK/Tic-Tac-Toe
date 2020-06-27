import random


# displays borad
def display(brd):
    print('T', ['0', '1', '2'])
    print(0, brd[0])
    print(1, brd[1])
    print(2, brd[2])


# takes in a player input and assign their markers as 'X' or 'O'
def player_input():
    positionX = int(input('enter the x value '))
    positionY = int(input('enter the y value '))
    return positionX, positionY


# X, Y = player_input()
# print(X, Y)

# takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9)
# and assigns it to the board
def place_marker(brd, mark, x, y):
    brd[x][y] = mark


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
def space_check(brd, x, y):
    if not full_board_check(brd):
        if brd[x][y] == ' ':
            return True
        else:
            return False


# print(space_check(board,1,2))

# asks for a player's next position and then uses the space_check function to check is it's a free position. If it
# is, then return the position for later use.
def player_choice(board, mark):
    ypos, xpos = player_input()
    xpos = int(xpos)
    ypos = int(ypos)
    if space_check(board, xpos, ypos):
        place_marker(board, mark, xpos, ypos)
    else:
        print('space already filled ')


# player_choice(testboard,'X')
# display(testboard)

# returns a boolean True if they do want to play again
def replay():
    replayStatement = 'Would you like to play again? Type yes or no '
    ans = input(replayStatement)
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

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
testboard = [row1, row2, row3]
display(testboard)

print('Welcome to Tic Tac Toe!')

# while True:
# Set the game up here
# pass
finished = False
playerturn = choose_first()
markerInputStatement = 'Which marker would you like to have? Type X or O '

if playerturn == 1:
    print('Player one goes first ')
    player1mark = input(markerInputStatement)
    print('Player two goes next ')
    player2mark = input(markerInputStatement)
    player1chance = True
    player2chance = False
else:
    print('Player two goes first')
    player2mark = input(markerInputStatement)
    print('Player one goes next')
    player1mark = input(markerInputStatement)
    player1chance = False
    player2chance = True
while not finished:
    display(testboard)
    while not win_check(testboard, player1mark) or win_check(testboard, player2mark):
        if player1chance:
            print('Player 1s turn ')
            player_choice(testboard, player1mark)
            player1chance = False
            player2chance = True
            display(testboard)
        elif player2chance:
            print('Player 2s turn ')
            player_choice(testboard, player2mark)
            player1chance = True
            player2chance = False
            display(testboard)
    if win_check(testboard, player1mark) or win_check(testboard, player2mark):
        row1 = [' ', ' ', ' ']
        row2 = [' ', ' ', ' ']
        row3 = [' ', ' ', ' ']
        testboard = [row1, row2, row3]
        if replay():
            finished = False
        else:
            finished = True
