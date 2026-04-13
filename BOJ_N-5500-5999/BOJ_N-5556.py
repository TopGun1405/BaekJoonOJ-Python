def main():
    N = int(input())
    K = int(input())
    tiles = [list(map(int, input().split())) for _ in range(K)]

    for a, b in tiles:
        if a > (N + 1) / 2:
            a = N + 1 - a
        if b > (N + 1) / 2:
            b = N + 1 - b

        if a > b:
            color = b % 3
        else:
            color = a % 3

        print(color if color else 3)


if __name__ == "__main__":
    main()
