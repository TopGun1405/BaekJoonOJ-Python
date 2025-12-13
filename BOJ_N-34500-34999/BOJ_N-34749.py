def main():
    N, M = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]

    s = 0
    for j in range(M):
        maxV = 0
        for i in range(N):
            maxV = max(maxV, G[i][j])
        s += maxV

    print(s)


if __name__ == "__main__":
    main()
