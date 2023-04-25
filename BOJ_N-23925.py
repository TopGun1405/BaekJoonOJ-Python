def main():
    T = int(input())
    for t in range(1, T + 1):
        N, K, S = map(int, input().split())
        print(f"Case #{t}: {min(K + N, K + (K - S) + (N - S))}")


if __name__ == "__main__":
    main()
