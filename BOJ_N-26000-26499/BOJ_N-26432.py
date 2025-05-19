def main():
    T = int(input())
    for x in range(1, T+1):
        M, N, P = map(int, input().split())
        scoreboard = [list(map(int, input().split())) for _ in range(M)]

        steps = 0
        for n in range(N):
            maxStep = 0
            for m in range(M):

                if m == P-1:
                    continue

                maxStep = max(maxStep, scoreboard[m][n])

            if maxStep > scoreboard[P-1][n]:
                steps += maxStep - scoreboard[P-1][n]

        print(f"Case #{x}: {steps}")


if __name__ == "__main__":
    main()
