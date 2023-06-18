def main():
    N = list(map(int, input().split()))
    for n in N:
        for i in range(n):
            if i == n - 1:
                print(' ' * i + '*')
            else:
                print(' ' * i + '*' + ' ' * (2 * (n - 1) - 1 - 2 * i) + '*')


if __name__ == "__main__":
    main()
