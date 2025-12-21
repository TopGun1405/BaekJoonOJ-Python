def main():
    n = int(input())
    a = list(map(int, input().split()))

    r = a.count(1)
    s = n // 2 + (1 if n % 2 else 0)

    print(max(0, s - r))


if __name__ == "__main__":
    main()
