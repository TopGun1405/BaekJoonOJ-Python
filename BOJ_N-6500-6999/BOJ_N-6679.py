def wow(n, m):
    tot = 0
    while n > 0:
        tot, n = tot + n % m, n // m
    return tot


def main():
    for n in range(1000, 10000):
        a, b, c = wow(n, 10), wow(n, 12), wow(n, 16)
        if a == b == c:
            print(n)


if __name__ == "__main__":
    main()
