def main():
    # incomplete
    Month, DD, YYYY, T = input().split()
    D, Y = int(DD[:-1]), int(YYYY)
    HH, MM = map(int, T.split(":"))

    month = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if Y % 400 == 0 or (Y % 100 != 0 and Y % 4 == 0):
        days[1] += 1

    times = sum(days) * 24 * 60
    idx = month.index(Month)
    curr_t = (sum(days[:idx]) + D-1) * 24 * 60 + HH * 60 + MM

    print(curr_t / times * 100)


if __name__ == "__main__":
    main()
