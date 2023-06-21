def main():
    N = int(input())
    iMap = [[0 for _ in range(501)] for _ in range(501)]
    minX, minY, maxX, maxY = 500, 500, 0, 0

    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        minX, minY = min(minX, x1), min(minY, y1)
        maxX, maxY = max(maxX, x2), max(maxY, y2)
        for i in range(x1, x2):
            for j in range(y1, y2):
                iMap[i][j] = 1

    cnt = 0
    for i in range(minX, maxX):
        for j in range(minY, maxY):
            if iMap[i][j]:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
