def main():
    K = int(input())
    for _ in range(K):
        N, M = map(int, input().split())

        if N == 1 or M == 1:
            print(0)
        else:
            print(2 * min(N-1, M-1))


if __name__ == "__main__":
    main()
