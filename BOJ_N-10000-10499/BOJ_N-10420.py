import datetime


def main():
    N = int(input())

    date = datetime.date(2014, 4, 2)

    print((date + datetime.timedelta(days=N-1)).strftime("%Y-%m-%d"))


if __name__ == "__main__":
    main()
