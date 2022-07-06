def main():
    N = int(input())
    ring = list(map(int, input().split()))

    for i in range(1, N):
        g = gcd(ring[0], ring[i])
        print("{}/{}".format(ring[0] // g, ring[i] // g))


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
