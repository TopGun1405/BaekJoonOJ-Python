def main():
    N, M = map(int, input().split())
    P, k = [0, 0], 0
    for n in range(N):
        C = list(map(int, input().split()))
        for m in range(M):
            if C[m] != 0:
                P[k], k = [n, m], k ^ 1
    print(abs(P[0][0] - P[1][0]) + abs(P[0][1] - P[1][1]))


if __name__ == "__main__":
    main()
