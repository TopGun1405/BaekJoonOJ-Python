def main():
    N = int(input())

    dice = [[0, 1, 3, 6, 10, 15], [0, 6, 11, 15, 18, 20]]
    result = 0
    for i in range(2):
        result += dice[i][5]
        result += dice[i][4] * (2 * (N - 1))
        result += dice[i][2] * (N - 1)
        result += dice[i][1] * 2 * ((N - 2) * (N - 1) // 2)
        result += dice[i][3] * ((N - 2) * (N - 1) // 2)

    print(result)


if __name__ == "__main__":
    main()
