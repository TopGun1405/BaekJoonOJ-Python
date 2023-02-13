def main():

    def QuadTree(n, row, col):
        color = bwVideo[row][col]
        m = n // 2
        for r in range(row, row + n):
            for c in range(col, col + n):
                if bwVideo[r][c] != color:
                    zipVideo.append('(')
                    QuadTree(m, row, col)
                    QuadTree(m, row, col + m)
                    QuadTree(m, row + m, col)
                    QuadTree(m, row + m, col + m)
                    zipVideo.append(')')
                    return
        zipVideo.append(str(color))

    N = int(input())
    bwVideo = [list(map(int, input().strip())) for _ in range(N)]
    zipVideo = []
    QuadTree(N, 0, 0)
    print(''.join(zipVideo))


if __name__ == "__main__":
    main()
