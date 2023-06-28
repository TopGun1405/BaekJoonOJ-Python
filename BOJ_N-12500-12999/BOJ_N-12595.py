def main():
    N = int(input())
    for n in range(1, N + 1):
        G = int(input())
        C = list(map(int, input().split()))
        alone = list(filter(lambda c: C.count(c) % 2, C))
        print("Case #{}: {}".format(n, alone[0]))


if __name__ == "__main__":
    main()
