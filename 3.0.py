board = [num for num in range(0, 10)]  # includes zero (unused) to avoid confusion with CS indexing
# board = ['X' for a in range(0, 10)]  # all Xs for testing
# board = [0, 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X']  # drawn board for testing
active = 0
move_list = []  # to store made moves
rematch = True

# TODO: entering 'num' and an input from move will return 9 (from the list comprehension) and I don't want it to


def board_print():
    print('\n {} | {} | {}'.format(board[1], board[2], board[3]))
    print('---|---|---')
    print(' {} | {} | {}'.format(board[4], board[5], board[6]))
    print('---|---|---')
    print(' {} | {} | {}\n'.format(board[7], board[8], board[9]))


def move_check():

    move_count = board.count('X') + board.count('O')  # could replace these later

    while move_count < 9:
        return True  # possible moves
    else:
        return False  # no moves


def gameover_check():

    # slicing rows, columns, & diagonals out of the board
    row1 = board[1:4]
    row2 = board[4:7]
    row3 = board[7:10]

    column1 = board[1::3]
    column2 = board[2::3]
    column3 = board[3::3]

    diagonal1 = board[1::4]
    diagonal2 = board[3:9:2]

    # Boolean equivalence checks: counts the number of times the first item in the list appears in the list and compares
    # it to the length of the list.
    r1_check = row1.count(row1[0]) == len(row1)
    r2_check = row2.count(row2[0]) == len(row2)
    r3_check = row3.count(row3[0]) == len(row3)
    c1_check = column1.count(column1[0]) == len(column1)
    c2_check = column2.count(column2[0]) == len(column2)
    c3_check = column3.count(column3[0]) == len(column3)
    d1_check = diagonal1.count(diagonal1[0]) == len(diagonal1)
    d2_check = diagonal2.count(diagonal2[0]) == len(diagonal2)

    while not r1_check and not r2_check and not r3_check and not c1_check and not c2_check and not c3_check and not \
            d1_check and not d2_check:
        return False  # no matches
    else:
        return True  # there is a match


def make_move():
    global active
    print("It is Player {}'s turn.".format(active + 1))

    while True:
        try:
            move = int(input('Select move (use number): '))  # need to validate this

        except SyntaxError:
            print('Syntax Error')
            continue

        except NameError:
            print('Name Error')
            continue

        except ValueError:
            print('Value Error')
            continue

        while not 0 < move < 10:
            print('Input out of range, please try again')
            continue

        if move in move_list:
            print('Move has already been made')
            continue

        else:
            move_list.append(move)

            if active == 0:
                board[move] = 'X'
            else:
                board[move] = 'O'

        break

    active = 1 - active


def new_game():
    return True


def game():

    for a in range(0, 9):

        print('\nBoard:')
        board_print()

        if not gameover_check():  # if there is no winner
            make_move()
        else:  # if there is a winner
            print('Game over. Player {} wins!'.format((1 - active) + 1))
            print('\nFinal board:')
            board_print()
            new_game()
            break  # exit the for loop

    else:
        print('\nBoard:')
        board_print()
        print('No moves possible, game is a draw.\n\nFinal board:')
        board_print()
        new_game()


game()
