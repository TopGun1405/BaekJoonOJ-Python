def main():
    while True:
        K = int(input())
        if K == 0:
            break
        N, M = map(int, input().split())
        for _ in range(K):
            X, Y = map(int, input().split())
            print("divisa" if X == N or Y == M
                  else ("SO" if X < N and Y < M
                        else "NO" if X < N else ("SE" if Y < M else "NE")))


if __name__ == "__main__":
    main()
