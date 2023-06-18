def main():
    N, M, K = map(int, input().split())
    print(((M - 1) + (K - 3) % N + N) % N + 1)


if __name__ == "__main__":
    main()
