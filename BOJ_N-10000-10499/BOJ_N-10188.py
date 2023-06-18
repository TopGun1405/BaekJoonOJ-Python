def main():
    n = int(input())
    for _ in range(n):
        col, row = map(int, input().split())
        for r in range(row):
            for c in range(col):
                print('X', end='')
            print()
        if _ < n - 1:
            print()


if __name__ == "__main__":
    main()
