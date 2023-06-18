def main():
    board = [list(map(int, input().split())) for _ in range(9)]
    coord0 = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]
    finish = [False]
    sudoku(0, board, coord0, finish)


def sudoku(n, b, c, f):

    if f[0]:
        return

    if n == len(c):
        f[0] = True
        for row in b:
            print(*row)
        return
    i, j = c[n]

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9):
        if b[i][k] in num:
            num.remove(b[i][k])
        if b[k][j] in num:
            num.remove(b[k][j])
    # print(num)

    v, h = i // 3, j // 3
    for p in range(v * 3, v * 3 + 3):
        for q in range(h * 3, h * 3 + 3):
            if b[p][q] in num:
                num.remove(b[p][q])
    # print(num)

    for s in num:
        b[i][j] = s
        sudoku(n + 1, b, c, f)
        b[i][j] = 0


if __name__ == "__main__":
    main()
