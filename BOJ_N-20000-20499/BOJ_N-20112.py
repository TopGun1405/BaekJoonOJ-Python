def main():
    N = int(input())
    mSquareR = [list(input()) for _ in range(N)]
    mSquareC = [[mSquareR[j][i] for j in range(N)] for i in range(N)]
    print(["NO", "YES"][mSquareR == mSquareC])


if __name__ == "__main__":
    main()
