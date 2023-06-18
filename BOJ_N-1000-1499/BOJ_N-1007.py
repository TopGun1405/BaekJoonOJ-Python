from itertools import combinations


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P, X, Y = [], 0, 0
        for _ in range(N):
            x, y = map(int, input().split())
            X, Y = X + x, Y + y
            P.append([x, y])

        combs = list(combinations(P, N // 2))
        minVector = 1e9
        for i in range(len(combs) // 2):
            x1, y1 = 0, 0
            for x, y in combs[i]:
                x1, y1 = x1 + x, y1 + y

            x2, y2 = X - x1, Y - y1
            minVector = min(minVector, ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        print(minVector)


if __name__ == "__main__":
    main()
