def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        S1 = N * (N + 1) // 2
        S2 = int((N * 2) * (N / 2))
        S3 = int((N * 2 + 2) * (N / 2))
        print(K, S1, S2, S3)


if __name__ == "__main__":
    main()
