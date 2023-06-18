def main():
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    p = S + [0] * M
    for i in range(N):
        T = list(map(int, input().split()))
        for j in range(N + M):
            p[i], p[j] = p[i] - T[j], p[j] + T[j]
    print(*p)


if __name__ == "__main__":
    main()
