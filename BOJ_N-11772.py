def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        P = int(input())
        ans += (P // 10) ** (P % 10)
    print(ans)


if __name__ == "__main__":
    main()
