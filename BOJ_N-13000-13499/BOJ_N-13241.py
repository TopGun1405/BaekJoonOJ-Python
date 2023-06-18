def main():
    A, B = map(int, input().split())
    g = gcd(A, B)
    print(A * B // g)


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
