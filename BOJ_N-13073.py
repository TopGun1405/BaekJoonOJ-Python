def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        S1 = N * (N + 1) // 2
        S2 = int((N * 2) * (N / 2))
        S3 = int((N * 2 + 2) * (N / 2))
        print(S1, S2, S3)


if __name__ == "__main__":
    main()
