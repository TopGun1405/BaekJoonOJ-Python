def main():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    countColor = {0: 0, 1: 0}

    def cuttingPaper(n: int, row: int, col: int):
        color = paper[row][col]
        m = n // 2
        for r in range(row, row + n):
            for c in range(col, col + n):
                if color != paper[r][c]:
                    cuttingPaper(m, row, col)
                    cuttingPaper(m, row, col + m)
                    cuttingPaper(m, row + m, col)
                    cuttingPaper(m, row + m, col + m)
                    return
        countColor[color] += 1

    cuttingPaper(N, 0, 0)
    print(*countColor.values(), sep='\n')


if __name__ == "__main__":
    main()
