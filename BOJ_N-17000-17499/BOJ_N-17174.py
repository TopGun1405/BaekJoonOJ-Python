def main():
    N, M = map(int, input().split())
    ans = N
    while N:
        N //= M
        ans += N
    print(ans)


if __name__ == "__main__":
    main()
