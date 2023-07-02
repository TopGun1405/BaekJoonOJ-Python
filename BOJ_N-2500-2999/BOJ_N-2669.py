def main():
    rect = [[0 for _ in range(101)] for _ in range(101)]

    for _ in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        for r in range(x1, x2):
            for c in range(y1, y2):
                rect[r][c] = 1

    s = 0
    for r in rect:
        s += sum(r)
    print(s)


if __name__ == "__main__":
    main()
