def main():
    n = int(input())
    print((2 ** (n // 2 + (1 if n % 2 else 0))) % 16_769_023)


if __name__ == "__main__":
    main()
