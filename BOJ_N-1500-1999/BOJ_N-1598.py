def main():
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))


if __name__ == "__main__":
    main()
