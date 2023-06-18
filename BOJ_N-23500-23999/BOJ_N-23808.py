def main():
    N = int(input())
    for i in range(N * 5):
        if 2 * N <= i < 3 * N or 4 * N <= i:
            print('@' * N * 5)
        else:
            print('@' * N + ' ' * N * 3 + '@' * N)


if __name__ == "__main__":
    main()
