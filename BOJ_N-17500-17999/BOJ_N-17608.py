def main():
    N = int(input())
    stick = [int(input()) for _ in range(N)]
    ans = 1
    temp = stick[-1]
    for i in range(N - 1, -1, -1):
        if stick[i] > temp:
            ans += 1
            temp = stick[i]
    print(ans)


if __name__ == "__main__":
    main()
