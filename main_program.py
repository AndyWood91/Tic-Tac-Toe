# Tic Tac Toe

# players
players = [{1: 'X'}, {2: 'O'}]

# board
# board = [[a for a in range(1, 4)] for b in range(1, 4)]  # sets each row to 1, 2, 3
# board = [[1 for a in range(1, 4)] for b in range(1, 4)]  # sets each row to 1, 1, 1
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # this way nothing matches to start
# I kinda know how to do this backwards but declaring it seems easier
indices = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}


def board_print():
    global players, board, indices
    print('\nCurrent board:')
    for row in board:
        print(row)
    return board


def game():
    global players, board, indices
    print('\nStarting a new game.')
    board_print()
    score_check()


def score_check():
    global players, board, indices
    # rows
    r1 = board[0]
    r2 = board[1]
    r3 = board[2]

    # columms
    c1 = [row[0] for row in board]
    c2 = [row[1] for row in board]
    c3 = [row[2] for row in board]

    # diagonals
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]

    # check for equivalence

    # rows
    r1_check = r1.count(r1[0]) == len(r1)
    r2_check = r2.count(r2[0]) == len(r2)
    r3_check = r3.count(r3[0]) == len(r3)

    # columns
    c1_check = c1.count(c1[0]) == len(c1)
    c2_check = c2.count(c2[0]) == len(c2)
    c3_check = c3.count(c3[0]) == len(c3)

    # diagonals
    d1_check = d1.count(d1[0]) == len(d1)
    d2_check = d2.count(d2[0]) == len(d2)

    if r1_check == False and r2_check == False and r3_check == False and c1_check == False and c2_check == False and \
        c3_check == False and d1_check == False and d2_check == False:
        print('\nno matches')
        make_move()
    else:
        print('\na match! Ending game')


def make_move():
    global board
    global active
    active = 0
    print('\nPlayer {}''s turn:'.format(players[active]))
    move = input('Enter the number of the position you would like to make a move in: ')
    active = 1 - active
    move_made = board[indices[move][0]][indices[move][1]] = players[active].values()
    return move_made

game()


# sequence



