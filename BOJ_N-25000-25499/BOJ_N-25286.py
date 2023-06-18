def main():
    T = int(input())
    d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for _ in range(T):
        y, m = map(int, input().split())
        if m == 1:
            print(y - 1, 12, 31)
        else:
            print(y, m - 1, end=' ')
            if ((y % 100 != 0 and y % 4 == 0) or y % 400 == 0) and m == 3:
                print(29)
            else:
                print(d[m - 1])


if __name__ == "__main__":
    main()
