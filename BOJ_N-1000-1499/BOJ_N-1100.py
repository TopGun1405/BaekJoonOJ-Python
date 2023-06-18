def main():
    board = [list(input()) for _ in range(8)]
    chess = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0 and board[i][j] == 'F':
                    chess += 1
            else:
                if j % 2 == 1 and board[i][j] == 'F':
                    chess += 1
    print(chess)


if __name__ == "__main__":
    main()
