def main():
    T = int(input())
    for x in range(1, T+1):
        N = int(input())

        minX, maxX = 1_000, -1_000
        minY, maxY = 1_000, -1_000
        for _ in range(N):
            X, Y = map(float, input().split())

            minX, maxX = min(minX, X), max(maxX, X)
            minY, maxY = min(minY, Y), max(maxY, Y)

        A, B = maxX - minX, maxY - minY
        print(f"Case {x}: Area {A*B}, Perimeter {2*(A+B)}")


if __name__ == "__main__":
    main()
