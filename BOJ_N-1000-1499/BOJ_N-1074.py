def main():
    N, r, c = map(int, input().split())
    visit = [0]

    def visitingZ(n: int, row: int, col: int):
        if not (row <= r < row + n and col <= c < col + n):
            visit[0] += n ** 2
            return
        if n == 2:
            for rr in range(row, row + n):
                for cc in range(col, col + n):
                    if rr == r and cc == c:
                        print(visit[0])
                        exit(0)
                    visit[0] += 1
        n //= 2
        visitingZ(n, row, col)
        visitingZ(n, row, col + n)
        visitingZ(n, row + n, col)
        visitingZ(n, row + n, col + n)

    visitingZ(2 ** N, 0, 0)


if __name__ == "__main__":
    main()
