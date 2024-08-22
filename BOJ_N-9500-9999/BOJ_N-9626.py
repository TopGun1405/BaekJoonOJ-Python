def main():

    def left(k, row):
        for l in range(L):
            if (k + row) % 2 == 0:
                print("#" if l % 2 == 0 else ".", end="")
            else:
                print("." if l % 2 == 0 else "#", end="")

    def mid(k, row):
        for n in range(N):
            if (k + row) % 2 == 0:
                print("#" if (L + n) % 2 == 0 else ".", end="")
            else:
                print("." if (L + n) % 2 == 0 else "#", end="")

    def right(k, row):
        for r in range(R):
            if (k + row) % 2 == 0:
                print("#" if (L + N + r) % 2 == 0 else ".", end="")
            else:
                print("." if (L + N + r) % 2 == 0 else "#", end="")

    M, N = map(int, input().split())
    U, L, R, D = map(int, input().split())
    puzzle = [input() for _ in range(M)]

    for u in range(U):
        left(u, 0)
        mid(u, 0)
        right(u, 0)
        print()

    for m in range(M):
        left(m, U)
        print(puzzle[m], end="")
        right(m, U)
        print()

    for d in range(D):
        left(d, U + M)
        mid(d, U + M)
        right(d, U + M)
        print()


if __name__ == "__main__":
    main()
