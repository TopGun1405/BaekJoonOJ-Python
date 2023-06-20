def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def main():
    n, m = map(int, input().split(':'))
    k = gcd(n, m)
    print(f'{n // k}:{m // k}')


if __name__ == "__main__":
    main()
