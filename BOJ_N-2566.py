def main():
    board = [list(map(int, input().split())) for _ in range(9)]
    max_v = -1
    v, h = 0, 0
    for i in range(9):
        for j in range(9):
            if board[i][j] > max_v:
                max_v = board[i][j]
                v, h = i + 1, j + 1
    print(max_v)
    print(v, h)


if __name__ == "__main__":
    main()
