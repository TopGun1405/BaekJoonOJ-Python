def main():
    m, n = int(input()), int(input())
    a, b = m - 2 if m >= 2 else 0, n - 2 if n >= 2 else 0
    print(m * n - a * b)


if __name__ == "__main__":
    main()
