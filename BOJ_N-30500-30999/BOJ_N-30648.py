def main():
    a, b = map(int, input().split())
    R = int(input())

    sec = 0
    garden = [[0 for _ in range(R)] for _ in range(R)]

    x_i, y_i = a, b
    while True:
        garden[x_i][y_i] += 1

        if garden[x_i][y_i] > 1:
            break

        if x_i + y_i + 2 < R:
            x_i += 1
            y_i += 1
        else:
            x_i //= 2
            y_i //= 2

        sec += 1

    print(sec)


if __name__ == "__main__":
    main()
