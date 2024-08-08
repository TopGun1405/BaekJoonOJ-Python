def main():
    N = int(input())

    # BOJ 10430: moduler operation
    # https://www.acmicpc.net/problem/10430
    dp = [[0]+[1]*9] + [[0]*10 for _ in range(N-1)]

    for i in range(1, N):
        dp[i][0] = dp[i-1][1]
        for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][9] = dp[i-1][8]

    print(sum(dp[N-1]) % 10**9)


if __name__ == "__main__":
    main()
