def main():
    N = int(input())
    menu = list(map(int, input().split()))

    cnt, maxStickers = 0, 0
    check = [False for _ in range(2 * N)]
    for m_i in menu:
        if not check[m_i]:
            cnt += 1
            check[m_i] = True
            maxStickers = max(cnt, maxStickers)
        else:
            cnt -= 1

    print(maxStickers)


if __name__ == "__main__":
    main()
