from itertools import combinations


def main():
    N, M = map(int, input().split())
    chickens = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for c1, c2, c3 in combinations(range(M), 3):
        v = 0
        for i in range(N):
            v += max(chickens[i][c1], chickens[i][c2], chickens[i][c3])
        maxV = max(maxV, v)

    print(maxV)


if __name__ == "__main__":
    main()
