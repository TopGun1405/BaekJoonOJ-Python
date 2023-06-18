def main():
    N = int(input())
    for i in range(N * 5):
        if i < N:
            print('@' * N * 3 + ' ' * N + '@' * N)
        elif 4 * N <= i:
            print('@' * N + ' ' * N + '@' * N * 3)
        else:
            print('@' * N + ' ' * N + '@' * N + ' ' * N + '@' * N)


if __name__ == "__main__":
    main()
