def main():
    N, a, b = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    x = X[a - 1][b - 1]
    A, B = [X[a - 1][j] for j in range(N)], [X[i][b - 1] for i in range(N)]
    print("ANGRY" if x < max(A) or x < max(B) else "HAPPY")


if __name__ == "__main__":
    main()
