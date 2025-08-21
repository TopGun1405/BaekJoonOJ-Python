def main():
    N = int(input())
    rad = []
    for _ in range(N):
        tokens = input().split()

        if tokens[1].isdigit():
            rad.append([tokens[0], int(tokens[1])])
        else:
            rad.append([tokens[1], int(tokens[0]) // 2])

    rad = list(map(lambda e: e[0], sorted(rad, key=lambda k: k[1])))

    print(*rad, sep="\n")


if __name__ == "__main__":
    main()
