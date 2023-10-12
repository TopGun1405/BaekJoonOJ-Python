def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    tot = 0
    for an, bn in zip(a, b):
        tot += abs(an - bn)
    print(tot // 2)


if __name__ == "__main__":
    main()
