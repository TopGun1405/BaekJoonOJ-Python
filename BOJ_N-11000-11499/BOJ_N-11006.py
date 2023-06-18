def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        L = 2 * M - N
        print(L, M - L)


if __name__ == "__main__":
    main()
