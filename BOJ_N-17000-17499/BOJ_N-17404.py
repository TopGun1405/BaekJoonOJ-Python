def main():
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    paint = [[1e9, 1e9, 1e9] for _ in range(N + 1)]
    minCost = 1e9

    for i in range(3):
        paint[1] = [1e9, 1e9, 1e9]
        paint[1][i] = cost[0][i]
        for j in range(2, N + 1):
            paint[j][0] = min(paint[j - 1][1], paint[j - 1][2]) + cost[j - 1][0]
            paint[j][1] = min(paint[j - 1][2], paint[j - 1][0]) + cost[j - 1][1]
            paint[j][2] = min(paint[j - 1][0], paint[j - 1][1]) + cost[j - 1][2]
        paint[N][i] = 1e9
        minCost = min(minCost, min(paint[N]))
    print(minCost)


if __name__ == "__main__":
    main()
