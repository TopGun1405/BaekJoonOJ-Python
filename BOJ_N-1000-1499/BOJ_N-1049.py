def main():
    N, M = map(int, input().split())

    minP, minU = 1_001, 1_001
    for _ in range(M):
        P, U = map(int, input().split())
        minP = min(minP, P)
        minU = min(minU, U)

    print(min(N // 6 * minP + N % 6 * minU, (N // 6 + 1) * minP, N * minU))


if __name__ == "__main__":
    main()
