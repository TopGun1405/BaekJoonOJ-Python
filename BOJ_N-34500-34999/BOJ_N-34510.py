def main():
    H1, H2, H3 = map(int, input().split())
    N = int(input())

    if N % 2 == 0:
        print(H2 * (N // 2) + H3 * N)
    else:
        print(H1 + H2 * (N // 2 + 1) + H3 * N)


if __name__ == "__main__":
    main()
