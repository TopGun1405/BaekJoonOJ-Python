def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        ans += sum(map(int, input().split()))
    print(ans)


if __name__ == "__main__":
    main()
