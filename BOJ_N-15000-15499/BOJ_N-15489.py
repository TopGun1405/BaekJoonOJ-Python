def main():
    R, C, W = map(int, input().split())

    pascal = [[1] * i for i in range(1, 32)]
    for i in range(2, 31):
        for j in range(1, len(pascal[i]) - 1):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    res = 0
    for i in range(R - 1, R + W - 1):
        for j in range(C - 1, C + i - R + 1):
            res += pascal[i][j]

    print(res)


if __name__ == "__main__":
    main()
