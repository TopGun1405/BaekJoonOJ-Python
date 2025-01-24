def main():
    a, b = map(int, input().split())
    d = int(input())

    print(((a * b) // 12 + (0 if a * b % 12 == 0 else 1)) * d)


if __name__ == "__main__":
    main()
