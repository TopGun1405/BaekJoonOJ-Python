def main():
    N, M, K = map(int, input().split())
    # if N >= M * K:
    #     n = N - (M * K)
    #     print(n, n + M - 1)
    # elif K == 1:
    #     print(0, N - 1)
    # else:
    #     print(0, 0)
    print(max(N - (M * K), 0), N - M * (K - 1) - 1)


if __name__ == "__main__":
    main()
