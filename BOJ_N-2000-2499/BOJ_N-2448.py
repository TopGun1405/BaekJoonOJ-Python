def main():

    def triStar(n, r, c):
        if n == 3:
            star[r][c] = '*'
            star[r + 1][c - 1:c + 2] = ['*', ' ', '*']
            star[r + 2][c - 2:c + 3] = ['*'] * 5
            return
        n //= 2
        triStar(n, r, c)
        triStar(n, r + n, c - n)
        triStar(n, r + n, c + n)

    N = int(input())
    star = [[' '] * 2 * N for _ in range(N)]
    triStar(N, 0, N - 1)
    for s in star:
        print(''.join(s))


if __name__ == "__main__":
    main()
