def main():
    num = int(input())
    n = 1
    while num != 1:
        n += 1
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    print(n)


if __name__ == "__main__":
    main()
