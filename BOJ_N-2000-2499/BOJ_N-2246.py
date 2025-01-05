def main():
    N = int(input())
    condo = sorted([list(map(int, input().split())) for _ in range(N)])

    cost, cnt = 10_001, 0
    for D, C in condo:
        if C < cost:
            cost = C
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
