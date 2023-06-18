def gcd(m, n):
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


def main():
    a, b = map(int, input().split())
    n = gcd(max(a, b), min(a, b))
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            print(i, a // i, b // i)
    print(n, a // n, b // n)


if __name__ == "__main__":
    main()
