def main():
    N = int(input())
    for i in range(N * 5):
        if N <= i < 2 * N or 3 * N <= i < 4 * N:
            print('@' * N * 5)
        else:
            print('@' * N + ' ' * N * 3 + '@' * N)


if __name__ == "__main__":
    main()
