def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    for n in range(max(X) + 1):
        ans = max(ans, X.count(n))
    print(ans)


if __name__ == "__main__":
    main()
