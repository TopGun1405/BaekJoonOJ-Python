def main() -> None:
    N = int(input())
    s = list(map(int, input().split()))
    cnt, x = 0, 0
    for si in s:
        if si == 0:
            cnt, x = max(cnt, x), 0
        else:
            x += 1
    print(max(cnt, x))


if __name__ == "__main__":
    main()
