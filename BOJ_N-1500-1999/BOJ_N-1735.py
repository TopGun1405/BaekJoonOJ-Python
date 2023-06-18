def gcd(n, m):
    if m == 0:
        return n
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def main():
    A1, B1 = map(int, input().split())
    A2, B2 = map(int, input().split())

    n, d = A1*B2 + A2*B1, B1*B2
    k = gcd(max(n, d), min(n, d))
    print(n // k, d // k)


if __name__ == "__main__":
    main()
