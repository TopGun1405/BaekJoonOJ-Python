def main():
    i = 1
    while True:
        n = int(input())
        if n == 0:
            break
        if n % 2 == 1:
            print("{}. odd {}".format(i, n // 2))
        else:
            print("{}. even {}".format(i, n // 2))
        i += 1


if __name__ == "__main__":
    main()
