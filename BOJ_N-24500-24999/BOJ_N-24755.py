def main():
    N = int(input())
    p = sorted(map(int, input().split()), reverse=True)

    cnt = 0
    for i in range(N):
        if i < N//2:
            cnt += p[i]
        else:
            cnt += p[i] // 2

    print(cnt)


if __name__ == "__main__":
    main()
