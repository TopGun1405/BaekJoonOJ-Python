def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        square = [list(map(int, input().split())) for _ in range(m)]

        magic = set()
        for i in range(m):
            magic.add(sum(square[i]))
            magic.add(sum([square[j][i] for j in range(m)]))

        magic.add(sum([square[i][i] for i in range(m)]))
        magic.add(sum([square[i][-i-1] for i in range(m)]))

        print(f"Magic square of size {m}" if len(magic) == 1 else "Not a magic square")


if __name__ == "__main__":
    main()
