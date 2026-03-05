def main():
    r, c = map(int, input().split())
    snakey = [list(input()) for _ in range(r)]

    s = []
    for y in range(c):
        for x in range(r):
            if snakey[x][y] != ".":
                s.append(snakey[x][y])

    print("".join(s))


if __name__ == "__main__":
    main()
