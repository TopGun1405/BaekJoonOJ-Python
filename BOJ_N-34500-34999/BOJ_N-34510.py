def main():
    H1, H2, H3 = map(int, input().split())
    N = int(input())

    # N % 2 == 0
    # H3 * N + H2 * (N - 1)
    # N % 2 == 1
    # H1 + H2 * (N - 1) + H3 * N
    # 1 : 1
    # 3 : 2
    # 5 : 3
    # 7 : 4

    if N % 2 == 0:
        print(H2 * (N // 2) + H3 * N)
    else:
        print(H1 + H2 * (N // 2 + 1) + H3 * N)


if __name__ == "__main__":
    main()
