def main():
    while True:
        try:
            n, k = map(int, input().split())

            num = n
            while n // k:
                num += n // k
                n = n // k + n % k
            print(num)

        except EOFError:
            break


if __name__ == "__main__":
    main()
    