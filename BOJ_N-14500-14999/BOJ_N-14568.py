def main():
    N = int(input())
    ans = 0
    for i in range(2, N - 1, 2):
        ans += (N - i - 2) // 2
    print(ans)


if __name__ == "__main__":
    main()
