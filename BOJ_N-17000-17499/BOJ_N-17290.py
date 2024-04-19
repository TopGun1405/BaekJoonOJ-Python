def main():
    r, c = map(int, input().split())
    field = [list(input()) for _ in range(10)]

    bomb = {'R': {n: False for n in range(10)},
            'C': {n: False for n in range(10)}}
    for row in range(10):
        for col in range(10):
            if field[row][col] == "x":
                continue
            if not bomb['R'].get(row, 1):
                del bomb['R'][row]
            if not bomb['C'].get(col, 1):
                del bomb['C'][col]

    minMove = 100
    r, c = r-1, c-1
    for row in bomb['R']:
        for col in bomb['C']:
            minMove = min(abs(r-row) + abs(c-col), minMove)

    print(minMove)


if __name__ == "__main__":
    main()
