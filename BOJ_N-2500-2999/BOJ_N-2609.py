def main():
    m, n = map(int, input().split())
    num = gcd(m, n)
    print(num)
    print(m * n // num)


def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


# def gcd(m, n):
#     while n != 0:
#         if m < n:
#             m, n = n, m
#         if n == 0:
#             return m
#         if m % n == 0:
#             return n


if __name__ == "__main__":
    main()
