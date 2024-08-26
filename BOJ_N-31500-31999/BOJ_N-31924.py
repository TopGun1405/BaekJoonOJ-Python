def main():
    N = int(input())
    board = [list(input()) for _ in range(N)]
    MOBIS = 0
    for i in range(N):
        for j in range(N):
            if 0 <= j < N-4 and "".join(board[i][j:j+5]) == "MOBIS":
                MOBIS += 1
            if j >= 4 and "".join(board[i][j-4:j+1][::-1]) == "MOBIS":
                MOBIS += 1
            if 0 <= i < N-4 and "".join([board[k][j] for k in range(i, i+5)]) == "MOBIS":
                MOBIS += 1
            if i >= 4 and "".join([board[k][j] for k in range(i, i-5, -1)]) == "MOBIS":
                MOBIS += 1
            if 0 <= i < N-4:
                if 0 <= j < N-4 and "".join(board[i+k][j+k] for k in range(5)) == "MOBIS":
                    MOBIS += 1
                if j >= 4 and "".join(board[i+k][j-k] for k in range(5)) == "MOBIS":
                    MOBIS += 1
            if i >= 4:
                if 0 <= j < N-4 and "".join(board[i-k][j+k] for k in range(5)) == "MOBIS":
                    MOBIS += 1
                if j >= 4 and "".join(board[i-k][j-k] for k in range(5)) == "MOBIS":
                    MOBIS += 1

    print(MOBIS)


if __name__ == "__main__":
    main()
