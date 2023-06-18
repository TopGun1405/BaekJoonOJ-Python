def ownSolution():
    N, K = map(int, input().split())

    P, Q = [], []
    for _ in range(N):
        Pi, Qi = map(int, input().split())
        P.append(Pi)
        Q.append(Qi)

    low, high = 0, 1
    while high - low > 0.000001:
        mid = (low + high) / 2

        lines = sorted([-Qi * mid + Pi for Pi, Qi in zip(P, Q)], reverse=True)

        totalP = totalQ = 0
        for i in range(K):
            totalP = totalP + lines[i][1]
            totalQ = totalQ + lines[i][2]

        if totalP / totalQ >= mid:
            low = mid
        else:
            high = mid
    print(low)


def main():
    N, K = map(int, input().split())
    PQ = [list(map(int, input().split())) for _ in range(N)]

    low, high = 0, 1
    for _ in range(20):
        mid = (low + high) / 2
        c = sum(sorted([-pq[1] * mid + pq[0] for pq in PQ], reverse=True)[:K])
        if c >= 0:
            low = mid
        else:
            high = mid
    print(low)


if __name__ == "__main__":
    main()
