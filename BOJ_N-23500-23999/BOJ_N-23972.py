def main():
    K, N = map(int, input().split())
    print(-1 if N == 1 else (K * N) // (N - 1) + (1 if (K * N) % (N - 1) else 0))


if __name__ == "__main__":
    main()
