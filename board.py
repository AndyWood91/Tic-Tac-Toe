board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# board = [[a for a in range(1, 4)] for b in range(1, 4)]

# indices
indices = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

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

move = input('enter position of move: ')

print(indices[move][0])

# def move_index(number):
#     try:
#         print('index of {} in {} is {}'.format(number, board, board.index(number)))
#         return board.index(number)
#     except:
#         ValueError
#         print('{} not found in {}'.format(number, board))
#         pass
#
# move_index(move)

