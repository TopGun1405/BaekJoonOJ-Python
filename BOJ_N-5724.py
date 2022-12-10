def main():
    while True:
        N = int(input())
        if N == 0:
            break
        ans = 0
        for i in range(1, N + 1):
            ans += (N - i + 1) ** 2
        print(ans)


if __name__ == "__main__":
    main()
