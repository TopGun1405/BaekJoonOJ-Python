def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))

        yen = 0
        for a_i in a:
            if a_i + yen <= 300:
                yen += a_i

        print(yen)


if __name__ == "__main__":
    main()
