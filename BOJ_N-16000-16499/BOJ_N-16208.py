def main():
    n = int(input())
    a = sorted(map(int, input().split()))

    minCost = 0
    while len(a) > 1:
        stick = []
        for ai, aj in zip(a[::2], a[1::2]):
            stick.append(ai + aj)
            minCost += ai * aj

        if len(a) % 2 == 1:
            stick.append(a[-1])
        a = sorted(stick)

    print(minCost)


if __name__ == "__main__":
    main()
