def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(a * b // gcd(a, b))


def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


if __name__ == "__main__":
    main()
