def main():
    N = int(input())
    n = 1
    while n * (n + 1) // 2 < N:
        n += 1
    b = N - (n - 1) * n // 2
    a = n + 1 - b
    print(a, b)


if __name__ == "__main__":
    main()
