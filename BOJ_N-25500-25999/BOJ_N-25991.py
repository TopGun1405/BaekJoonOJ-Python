def main():
    n = int(input())
    num = sum(map(lambda e: e ** 3, list(map(float, input().split()))))
    print(num ** (1 / 3))


if __name__ == "__main__":
    main()
