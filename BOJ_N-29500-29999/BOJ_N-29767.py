def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [A[0]] + [0] * (N-1)
    for i in range(1, N):
        dp[i] = dp[i-1] + A[i]

    dp.sort(reverse=True)
    print(sum(dp[:K]))


if __name__ == "__main__":
    main()
