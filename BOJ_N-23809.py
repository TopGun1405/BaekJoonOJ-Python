def main():
    N = int(input())
    for i in range(N * 5):
        if 2 * N <= i < 3 * N:
            print('@' * N * 3)
        elif N <= i < 2 * N or 3 * N <= i < 4 * N:
            print('@' * N + ' ' * N * 2 + '@' * N)
        else:
            print('@' * N + ' ' * N * 3 + '@' * N)


if __name__ == "__main__":
    main()
