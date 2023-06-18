def main():
    N, M = map(int, input().split())
    limit = [list(map(int, input().split())) for _ in range(N)]
    jung_v = [list(map(int, input().split())) for _ in range(M)]
    i, j, m = 0, 0, 0
    while i < N and j < M:
        if v > limit[i][1] and v - limit[i][1] > m:
            m = v - limit[i][1]
        if limit[i][0] == 0 and i < N:
            i += 1


if __name__ == "__main__":
    main()
