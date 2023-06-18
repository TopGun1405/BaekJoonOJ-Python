def main():
    N = int(input())
    maxX, minX = -10_000, 10_000
    maxY, minY = -10_000, 10_000
    for _ in range(N):
        x, y = map(int, input().split())
        maxX = x if x > maxX else maxX
        minX = x if x < minX else minX
        maxY = y if y > maxY else maxY
        minY = y if y < minY else minY
    print((maxX - minX) * (maxY - minY))


if __name__ == "__main__":
    main()
