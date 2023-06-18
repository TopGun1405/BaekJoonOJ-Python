def main():
    n = int(input())
    while True:
        num = int(input())
        if num == 0:
            break
        print("{} is a multiple of {}.".format(num, n) if num % n == 0
              else "{} is NOT a multiple of {}.".format(num, n))


if __name__ == "__main__":
    main()
