def main():
    d, m, y, n = map(int, input().split())
    date = list(map(int, input().split()))

    to_days = lambda D, M, Y: Y*360 + (M-1)*30 + (D-1)

    d1 = to_days(d, m, y)
    d2 = to_days(date[0], date[1], date[2])

    print((n - 1 + (d2 - d1)) % 7 + 1)


if __name__ == "__main__":
    main()
