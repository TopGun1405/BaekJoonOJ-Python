def main():
    N = int(input())
    for i in range(N * 5):
        if i < N or i >= N * 4:
            print('@' * N * 5)
        else:
            print('@' * N + ' ' * N * 3 + '@' * N)


if __name__ == "__main__":
    main()
