def main():
    NR, NC = map(int, input().split())
    grass = [list(map(int, input().split())) for _ in range(NR)]

    bestGrid = 0
    row, col = 0, 0
    for r in range(NR-3):
        for c in range(NC-3):
            grid = sum([grass[i][j] for i in range(r, r+3) for j in range(c, c+3)])

            if grid > bestGrid:
                bestGrid = grid
                row, col = r, c

    print(bestGrid)
    print(row+1, col+1)


if __name__ == "__main__":
    main()
