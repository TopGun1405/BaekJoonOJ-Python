def main():
    n, m = map(int, input().split())

    # out of memory
    # arr = [[1], [1, 1]]
    # for i in range(2, n + 1):
    #     arr.append([1 if j == 0 or j == i
    #                 else arr[i - 1][j - 1] + arr[i - 1][j]
    #                 for j in range(i + 1)])
    # num = list(str(arr[n][m]))
    i = 0
    u2, u5 = 0, 0
    d2, d5 = 0, 0
    while True:
        i += 1
        if 2 ** i <= n:
            u2 += n // (2 ** i)
        if 5 ** i <= n:
            u5 += n // (5 ** i)
        if 2 ** i <= m:
            d2 += m // (2 ** i)
        if 5 ** i <= m:
            d5 += m // (5 ** i)
        if 2 ** i <= n - m:
            d2 += (n - m) // (2 ** i)
        if 5 ** i <= n - m:
            d5 += (n - m) // (5 ** i)
        if 2 ** i > n and 5 ** i > n and 2 ** i > m and 5 ** i > m and 2 ** i > n - m and 5 ** i > n - m:
            break
    print(min(u2 - d2, u5 - d5))


if __name__ == "__main__":
    main()
