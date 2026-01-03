def main():
    a, b, n, k = map(int, input().split())

    x = k // n + (1 if k % n else 0)
    i, j = x // b + (1 if x % b else 0), x % b + (b if x % b == 0 else 0)

    print(i, j)


if __name__ == "__main__":
    main()
