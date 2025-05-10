def main():
    T = int(input())
    for _ in range(T):
        N = int(input())

        money, M = 100_001, 0
        for _ in range(N):
            W, C = map(int, input().split())

            if money > C / W:
                money, M = C / W, C
            elif money == C / W and M > C:
                M = C

        print(M)


if __name__ == "__main__":
    main()
