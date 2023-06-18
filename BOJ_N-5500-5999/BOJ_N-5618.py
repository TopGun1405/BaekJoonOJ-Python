def main():
    n = int(input())
    if n == 2:
        a, b = map(int, input().split())
        k = gcd(a, b)
        num = [i for i in range(1, k + 1) if k % i == 0]
        print(*num, sep='\n')
    elif n == 3:
        t = list(map(int, input().split()))
        while True:
            if t[0] == t[1] == t[2]:
                break
            i, j, k = gcd(t[0], t[1]), gcd(t[1], t[2]), gcd(t[2], t[0])
            t[0], t[1], t[2] = i, j, k
        num = [i for i in range(1, t[0] + 1) if t[0] % i == 0]
        print(*num, sep='\n')

    # input()
    # a = list(map(int, input().split()))
    # g = a[0]
    # for i in range(1, len(a)):
    #     g = math.gcd(g, a[i])
    # s = set()
    # for i in range(1, int(g ** 0.5) + 1):
    #     if g % i == 0:
    #         s.update([i, g // i])
    # for i in sorted(s):
    #     print(i)


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
