def main():
    N, K = map(int, input().split())

    F = [K] + [0] * (N-1)
    for i in range(1, N):
        F[i] = F[i-1]//2

    print(F[N-1])


if __name__ == "__main__":
    main()
