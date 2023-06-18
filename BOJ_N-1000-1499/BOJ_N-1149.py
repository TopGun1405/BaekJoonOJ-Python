def main():
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    paint = [[0, 0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        paint[i][0] = min(paint[i - 1][1], paint[i - 1][2]) + cost[i - 1][0]
        paint[i][1] = min(paint[i - 1][2], paint[i - 1][0]) + cost[i - 1][1]
        paint[i][2] = min(paint[i - 1][0], paint[i - 1][1]) + cost[i - 1][2]
    print(min(paint[N][0], paint[N][1], paint[N][2]))


if __name__ == "__main__":
    main()
