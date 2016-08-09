# Declarations
players = [{1: 'X'}, {2: 'O'}]
active = 0
# board = [['-' for a in range(1, 4)] for b in range(1, 4)]
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]  # this way nothing matches to start
# board = [[1 for a in range(1, 4)] for b in range(1, 4)]
# I sort of know how to work this out in reverse but I think it's easier to just declare it
board_indices = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}


def board_print():
    global players, active, board, board_indices
    print('\nCurrent board state:')
    for row in board:
        print(row)
    return


def game_over_check():
    global players, active, board, board_indices
    print('\nIs the game over?')

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

    # # move_check =
    # for row in board:
    #     row[0].count('X')
    #     print(row)
    #     print(row.count('X'))

    # TODO: check to see if any moves are possible
    # Boolean, if board.count('-') == 0, end game
    # probably best to put this within the other check
    # TODO: this count doesn't work because it's not searching within rows
    print('X count is {}, O count is {}'.format(board.count(players[0].values()), board.count(players[1].values())))
    print('X count is {}'.format(board.count('X')))
    print('O count is {}'.format(board.count('O')))

    while not r1_check and not r2_check and not r3_check and not c1_check and not c2_check and not c3_check and \
            not d1_check and not d2_check:
        print('No matches.\nGame continues.')
        return False
    else:
        print('There is a match!\nGame over.\nPlayer {} wins'.format(players[active - 1].keys()))
        return True


def make_move():
    global players, active, board, board_indices
    print('\nIt is player {}''s turn'.format(players[active].keys()))
    board_print()
    # TODO: stop allowing duplicate moves to be made
    move = input('select move (use number): ')
    try:

        board[board_indices[move][0]][board_indices[move][1]] = players[active].values()
    except:
        ValueError
        move = input('out of range: select move (use number): ')

    board_indices.pop(move)
    print('board indicies: {}'.format(board_indices))
    active = 1 - active
    return


def game():
    global players, active, board, board_indices
    board_print()
    while not game_over_check():
        make_move()
    else:
        return



game()
