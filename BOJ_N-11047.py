def main():
    N, K = map(int, input().split())
    money = [int(input()) for _ in range(N)]
    ans = 0
    for i in range(N - 1, -1, -1):
        if K >= money[i]:
            ans += K // money[i]
            K %= money[i]
        elif K == 0:
            break
    print(ans)


if __name__ == "__main__":
    main()
