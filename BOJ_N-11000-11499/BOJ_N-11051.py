def main():

    ##############
    # solution 1 #
    ##############

    #      1                             (0, 0)
    #     1  1                       (1, 0), (1, 1)
    #    1  2  1                 (2, 0), (2, 1), (2, 2)
    #   1  3  3  1           (3, 0), (3, 1), (3, 2), (3, 3)
    #  1  4  6  4  1     (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)

    N, K = map(int, input().split())
    arr = [[1], [1, 1]]

    for i in range(2, N + 1):
        arr.append([1 if j == 0 or j == i
                    else arr[i - 1][j - 1] + arr[i - 1][j]
                    for j in range(i + 1)])
    print(arr[N][K] % 10_007)

    ##############
    # solution 2 #
    ##############

    N, K = map(int, input().split())
    numerator = 1
    for i in range(1, N + 1):
        numerator *= i
    denominator = 1
    for i in range(1, K + 1):
        denominator *= i
    deno2 = 1
    for i in range(1, N - K + 1):
        deno2 *= i
    print(numerator // (denominator * deno2) % 10007)


if __name__ == "__main__":
    main()
