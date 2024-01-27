def is_safe(board, row, col):
    return all(
        board[i] != col and board[i] - i != col - row and board[i] + i != col + row
        for i in range(row)
    )

def solve_nqueens(board, row):
    n = len(board)
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)

def nqueens():
    n = 4
    solve_nqueens([-1] * n, 0)

nqueens()
