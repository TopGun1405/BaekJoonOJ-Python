from datetime import date


def main():

    def d(d1, d2):
        return (d2-d1).days

    while True:
        D, M, Y = map(int, input().split())

        if D == M == Y == 0:
            break

        date1, date2 = date(Y, 1, 1), date(Y, M, D)
        print(d(date1, date2) + 1)


if __name__ == "__main__":
    main()
