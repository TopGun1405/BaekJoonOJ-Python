def main():
    N = int(input())
    par = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += (7 if par[i] > 7 else par[i]) - (3 if i % 2 else 2)
    print(ans)


if __name__ == "__main__":
    main()
