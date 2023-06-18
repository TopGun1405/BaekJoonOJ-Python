def main():
    N = int(input())
    for i in range(N):
        if i == 0:
            print('*' * N + ' ' * (2 * (N - 1) - 1) + '*' * N)
        elif i == N - 1:
            print(' ' * i + '*' + ' ' * (N - 2) + '*' + ' ' * (N - 2) + '*')
        else:
            print(' ' * i + '*' + ' ' * (N - 2) + '*' + ' ' * (2 * (N - i - 1) - 1) + '*' + ' ' * (N - 2) + '*')
    for i in range(N - 2, -1, -1):
        if i == 0:
            print('*' * N + ' ' * (2 * (N - 1) - 1) + '*' * N)
        else:
            print(' ' * i + '*' + ' ' * (N - 2) + '*' + ' ' * (2 * (N - i - 1) - 1) + '*' + ' ' * (N - 2) + '*')


if __name__ == "__main__":
    main()
