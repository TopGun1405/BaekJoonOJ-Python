def main():
    N, M = map(int, input().split())
    K = list(map(int, input().split()))
    ans = 0
    for n in range(1, N + 1):
        for k in K:
            if n % k == 0:
                ans += n
                break
    print(ans)


if __name__ == "__main__":
    main()
