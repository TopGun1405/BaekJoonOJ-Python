def main():

    def sudoku(n):
        if n == len(zeroPos):
            for row in board:
                print(*row, sep='')
            exit(0)
        i, j = zeroPos[n]

        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for k in range(9):
            if board[i][k] in num:
                num.remove(board[i][k])
            if board[k][j] in num:
                num.remove(board[k][j])

        v, h = i // 3, j // 3
        for p in range(v * 3, v * 3 + 3):
            for q in range(h * 3, h * 3 + 3):
                if board[p][q] in num:
                    num.remove(board[p][q])

        # backtracking
        for s in num:
            board[i][j] = s
            sudoku(n + 1)
            board[i][j] = 0

    board = [list(map(int, input().strip())) for _ in range(9)]
    zeroPos = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]
    sudoku(0)


if __name__ == "__main__":
    main()
