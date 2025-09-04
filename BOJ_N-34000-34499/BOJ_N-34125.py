def main():
    N, M = map(int, input().split())
    seat = [list(map(int, input().split())) for _ in range(N)]

    R, C = 0, 0
    minDis = 1_000
    for r in range(1, N+1):
        for c in range(1, M+1):
            if seat[r-1][c-1] == 0:
                Distance = r + abs((M + 1) // 2 - c)
                if Distance < minDis:
                    minDis = Distance
                    R, C = r, c

    if R == C == 0:
        print(-1)
    else:
        print(R, C)


if __name__ == "__main__":
    main()
