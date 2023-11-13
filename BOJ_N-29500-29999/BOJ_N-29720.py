def main():
    N, M, K = map(int, input().split())
    print(max(N - (M * K), 0), N - M * (K - 1) - 1)


if __name__ == "__main__":
    main()
