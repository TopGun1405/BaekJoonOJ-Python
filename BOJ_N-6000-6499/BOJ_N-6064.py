def main():
    T = int(input())
    for _ in range(T):
        M, N, x, y = map(int, input().split())
        for k in range(x, M * N + 1, M):
            if (k - x) % M == (k - y) % N == 0:
                print(k)
                break
        else:
            print(-1)


if __name__ == "__main__":
    main()
