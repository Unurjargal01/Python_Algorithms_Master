def cover(board, lab = 1, top = 0, left = 0, s = None):
    print(lab)
    if s is None: s = len(board)

    side = s // 2

    offsets = [0, -1], [s - 1, 0]

    for y_outer, y_inner in offsets:
        for x_outer, x_inner in offsets:
            if not board[top + y_outer][left + x_outer]:
                board[top + side + y_inner][left + side + x_inner] = lab

    lab += 1
    if side > 1:

        for x in [0, side]:
            for y in [0, side]:
                lab = cover(board, lab, top + y, left + x, side)
    return lab
board = [[0] * 8 for i in range(8)]
board[-1][-1] = -1
cover(board)

for row in board:
    print((" %2i" * 8) % tuple(row))