def main():
    n = int(input())
    print(chr((n % 8 if n % 8 else 8) + 96) + str(n // 8 + (1 if n % 8 else 0)))


if __name__ == "__main__":
    main()
