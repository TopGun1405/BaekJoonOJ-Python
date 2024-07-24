def main():
    R, C = map(int, input().split())
    card = list(map(lambda s: s+s[::-1], [list(input()) for _ in range(R)]))
    A, B = map(int, input().split())

    trans = {'.': "#", '#': "."}
    card += [row[::] for row in card][::-1]
    card[A-1][B-1] = trans[card[A-1][B-1]]

    for row in card:
        print("".join(row))


if __name__ == "__main__":
    main()