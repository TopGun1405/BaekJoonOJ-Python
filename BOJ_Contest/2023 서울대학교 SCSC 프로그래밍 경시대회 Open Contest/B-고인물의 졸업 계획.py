def main():
    N, M = map(int, input().split())
    S = [int(input()) for _ in range(M)]
    p = [[[], 0]] * (M + 1)
    print(p)
    for i, s in enumerate(S):
        if p[i][1] < N and p[i][1] <= 2*N:
            p[i][0].append(i + 1)
            p[i][1] += s
    print(p)


if __name__ == "__main__":
    main()
