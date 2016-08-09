board = [[a for a in range(1, 4)], [b for b in range(4, 7)], [c for c in range(7, 10)]]


# returns nothing
def board_print():
    for row in board:
        print(row)
    return


def game():
    print('Starting a ')
    board_print()
    return

game()

board_print()