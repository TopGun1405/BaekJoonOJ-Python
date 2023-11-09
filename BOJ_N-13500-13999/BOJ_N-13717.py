def main():
    N = int(input())

    tot, maxEvo = 0, [0, '']
    for _ in range(N):
        Pi = input()
        Ki, M = map(int, input().split())

        evolve = (M - Ki) // (Ki - 2) + 1
        if evolve > 0:
            tot += evolve

            if maxEvo[0] < evolve:
                maxEvo[0] = evolve
                maxEvo[1] = Pi

    print(tot)
    print(maxEvo[1])


if __name__ == "__main__":
    main()
