def main():
    N = int(input())
    for _ in range(N):
        num1, num2 = input().split('-')
        first = sum(map(lambda c, i: (ord(c) - 65) * 26 ** i, num1, list(range(len(num1) - 1, -1, -1))))
        print(["not nice", "nice"][abs(first - int(num2)) <= 100])


if __name__ == "__main__":
    main()
