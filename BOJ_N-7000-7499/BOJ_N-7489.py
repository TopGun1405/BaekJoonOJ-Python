def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        res = 1
        for i in range(1, n+1):
            res *= i
            res %= 1_000_000_000_000
            while res % 10 == 0:
                res /= 10

        print(int(res % 10))


if __name__ == "__main__":
    main()
