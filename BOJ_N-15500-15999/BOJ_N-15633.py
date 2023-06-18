def main():
    n = int(input())
    num = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            num += i
            if i ** 2 != n:
                num += n // i
    print(num * 5 - 24)


if __name__ == "__main__":
    main()
