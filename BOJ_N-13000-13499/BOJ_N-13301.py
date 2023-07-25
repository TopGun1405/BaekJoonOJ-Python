def main():
    N = int(input())

    tile = [0, 4, 6] + [0] * 78
    for i in range(3, N + 1):
        tile[i] = tile[i - 1] + tile[i - 2]

    print(tile[N])


if __name__ == "__main__":
    main()
