def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = list(map(int, input().split()))
        d = 0
        minD, maxD = 100, 0
        for i in range(n):
            d += x[i]
            if minD > x[i]:
                minD = x[i]
            if maxD < x[i]:
                maxD = x[i]
        s = d // n
        print(2 * (maxD - s) + 2 * (s - minD))


if __name__ == "__main__":
    main()
