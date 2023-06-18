def main():
    n = int(input())
    lev = 0
    while True:
        if n < 10:
            break
        temp = list(map(int, list(str(n))))
        n = 1
        for i in temp:
            n *= i
        lev += 1
    print(lev)


if __name__ == "__main__":
    main()
