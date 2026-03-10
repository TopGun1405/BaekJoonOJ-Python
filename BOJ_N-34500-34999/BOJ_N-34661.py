def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        board = [list(input()) for _ in range(N)]

        blank = 0
        for i in range(N):
            blank += board[i].count(".")

        print("sewon" if blank % 2 == 1 else "pizza")


if __name__ == "__main__":
    main()
