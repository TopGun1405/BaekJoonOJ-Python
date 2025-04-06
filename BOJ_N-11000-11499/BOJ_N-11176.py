def main():
    T = int(input())
    for _ in range(T):
        E, N = map(int, input().split())

        empty = 0
        for _ in range(N):
            attempt = int(input())
            if attempt > E:
                empty += 1

        print(empty)


if __name__ == "__main__":
    main()
