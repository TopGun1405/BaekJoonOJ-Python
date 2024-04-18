def main():
    N, R = map(int, input().split())
    pos = []
    minX, minY = 100, 100
    maxX, maxY = -100, -100
    for _ in range(N):
        xi, yi = map(int, input().split())
        minX, minY = min(xi, minX), min(yi, minY)
        maxX, maxY = max(xi, maxX), max(yi, maxY)
        pos.append([xi, yi])

    maxRice = 0
    rx, ry = 0, 0
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):

            riceCnt = 0
            for xi, yi in pos:
                r = ((x - xi)**2 + (y - yi)**2)**0.5
                if r <= R:
                    riceCnt += 1

            if riceCnt > maxRice:
                maxRice = riceCnt
                rx, ry = x, y

    print(rx, ry)


if __name__ == "__main__":
    main()
