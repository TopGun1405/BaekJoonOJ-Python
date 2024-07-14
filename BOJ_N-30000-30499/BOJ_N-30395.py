def main():
    N = int(input())
    P = list(map(int, input().split()))
    maxStrict, currStrict, f = 0, 0, -2

    for i in range(N):
        if P[i]:
            currStrict += 1
        elif i-f >= 2:
            f = i
        else:
            currStrict = 0
        maxStrict = max(maxStrict, currStrict)

    print(maxStrict)


if __name__ == "__main__":
    main()
