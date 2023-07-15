def main():
    N = int(input())

    dp = [0] * 1_000_001
    dp[1], dp[2] = 1, 2

    for k in range(3, N + 1):
        dp[k] = (dp[k-1] + dp[k-2]) % 15746

    print(dp[N])


if __name__ == "__main__":
    main()
