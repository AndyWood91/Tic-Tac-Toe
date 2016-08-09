players = [{1: 'X'}, {2: 'O'}]
active_player = 0

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
indices = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

for row in board:
    print(row)

move = input('enter position: ')

print(indices[move][0])
print(indices[move][1])

board[indices[move][0]][indices[move][1]] = players[active_player].values()

print(board)
