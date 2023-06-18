def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    for _ in range(K):
        i, j, x, y = map(int, input().split())
        ans = 0
        for p in range(i - 1, x):
            for q in range(j - 1, y):
                ans += arr[p][q]
        print(ans)


if __name__ == "__main__":
    main()
