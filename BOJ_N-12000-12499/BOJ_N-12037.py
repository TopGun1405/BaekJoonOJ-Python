def main():
    T = int(input())

    MOD = 1_000_000_007
    dp = [[0] * 2 for _ in range(16)]
    for x in range(1, T+1):
        C, V, L = map(int, input().split())

        dp[1][0], dp[1][1] = V, C
        for i in range(2, L+1):
            dp[i][0] = ((V % MOD) * ((dp[i-1][0] % MOD + dp[i-1][1] % MOD) % MOD)) % MOD
            dp[i][1] = ((C % MOD) * (dp[i-1][0] % MOD)) % MOD

        print(f"Case #{x}: {dp[L][0]}")


if __name__ == "__main__":
    main()
