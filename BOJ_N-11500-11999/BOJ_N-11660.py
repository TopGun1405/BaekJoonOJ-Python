def main():
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] = table[i][j] + dp[i][j+1] + dp[i+1][j] - dp[i][j]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])


if __name__ == "__main__":
    main()
