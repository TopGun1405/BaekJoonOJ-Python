def main():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    countPaper = {-1: 0, 0: 0, 1: 0}

    def cuttingPaper(n, row, col):
        pType = paper[row][col]
        m = n // 3
        for r in range(row, row + n):
            for c in range(col, col + n):
                if pType != paper[r][c]:
                    cuttingPaper(m, row, col)
                    cuttingPaper(m, row, col + m)
                    cuttingPaper(m, row, col + 2 * m)
                    cuttingPaper(m, row + m, col)
                    cuttingPaper(m, row + m, col + m)
                    cuttingPaper(m, row + m, col + 2 * m)
                    cuttingPaper(m, row + 2 * m, col)
                    cuttingPaper(m, row + 2 * m, col + m)
                    cuttingPaper(m, row + 2 * m, col + 2 * m)
                    return
        countPaper[pType] += 1

    cuttingPaper(N, 0, 0)
    print(*countPaper.values(), sep='\n')


if __name__ == "__main__":
    main()
