def main():
    n = int(input())
    m = int(input())

    print(2 * min(n, m) + (1 if abs(n - m) % 2 == 1 else 0))


if __name__ == "__main__":
    main()
