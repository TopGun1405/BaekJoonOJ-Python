def main():
    N, M = map(int, input().split())
    P = sorted([int(input()) for _ in range(M)])

    maxC, P_i = 0, 0
    for i in range(M):
        c = min(M-i, N)
        if maxC < P[i] * c:
            maxC, P_i = P[i] * c, P[i]

    print(P_i, maxC)


if __name__ == "__main__":
    main()
