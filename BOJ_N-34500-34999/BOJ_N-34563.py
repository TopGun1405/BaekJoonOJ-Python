def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        print(N + M - 1)


if __name__ == "__main__":
    main()
