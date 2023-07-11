def main():
    N = int(input())
    minX, minY, maxX, maxY = 100, 100, 0, 0
    for _ in range(N):
        X, Y = map(int, input().split(','))
        minX, minY = min(minX, X), min(minY, Y)
        maxX, maxY = max(maxX, X), max(maxY, Y)
    print(f"{minX-1},{minY-1}")
    print(f"{maxX+1},{maxY+1}")


if __name__ == "__main__":
    main()
