def main():
    N, M, K = map(int, input().split())
    print(N // (K - M) + (0 if N % (K - M) == 0 else 1))


if __name__ == "__main__":
    main()
