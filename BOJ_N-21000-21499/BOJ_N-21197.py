def main():
    N = int(input())
    t = [int(input()) for _ in range(N)]
    if N % 2 == 1:
        print("still running")
        exit(0)
    ans = 0
    for i in range(1, N, 2):
        ans += t[i] - t[i - 1]
    print(ans)


if __name__ == "__main__":
    main()