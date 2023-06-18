def main():
    while True:
        n = int(input())
        if n == 0:
            break
        while n > 9:
            n = sum(map(int, str(n)))
        print(n)


if __name__ == "__main__":
    main()
