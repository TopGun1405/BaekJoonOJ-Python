def main():
    N, M = map(int, input().split())
    dis = [list(map(int, input().split())) for _ in range(N)]

    r, c = 0, 0
    r_min, c_min = 50, 50
    for i in range(N):
        if dis[i][0] < r_min:
            r = i
            r_min = dis[i][0]

    for j in range(M):
        if dis[N-1][j] < c_min:
            c = j
            c_min = dis[N-1][j]

    print(r+1, c+1)


if __name__ == "__main__":
    main()
