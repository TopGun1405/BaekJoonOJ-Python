def main():
    # x * M + c = y
    # z * M + c = w
    #
    # c = y - x * M
    # c = w - z * M
    #
    # y - x * M = w - z * M
    # y - w = (x - z) * M
    # (y - w) / (x - z) = M
    N = int(input())
    num = [int(input()) for _ in range(N)]
    temp = []
    for i in range(N - 1):
        # print(num[i], num[i + 1])
        temp.append(abs(num[i] - num[i + 1]))
    temp.sort()
    # print(temp)

    smallest = 0
    # when N == 2
    if len(temp) > 1:
        smallest = gcd(temp[0], temp[1])
        for i in range(2, len(temp)):
            n = gcd(temp[0], temp[i])
            if n < smallest:
                smallest = n
    elif len(temp) == 1:
        smallest = temp[0]
    # print(smallest)

    # *****
    divisor = {smallest}
    for s in range(2, int(smallest ** 0.5) + 1):
        if smallest % s == 0:
            divisor.add(s)
            divisor.add(smallest // s)
    print(*sorted(divisor), sep=' ')


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