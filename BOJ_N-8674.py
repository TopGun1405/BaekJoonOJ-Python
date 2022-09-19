def main():
    a, b = map(int, input().split())
    print(min(a, b) if a % 2 == 1 and b % 2 == 1 else 0)


if __name__ == "__main__":
    main()
