def main():
    N = int(input())
    for i in range(N * 5):
        if i < N or 2 * N <= i < 3 * N or 4 * N <= i:
            print('@' * N * 5)
        else:
            print('@' * N)


if __name__ == "__main__":
    main()
