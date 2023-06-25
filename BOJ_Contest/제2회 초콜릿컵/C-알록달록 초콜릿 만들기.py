def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        mintCnt, cnt = 0, 0
        i = 0
        while mintCnt < n:
            cnt, i = cnt + i, i + 1
            if i % 2:
                mintCnt += int(1 + i / 6 * 2)
            else:
                mintCnt += int((i / 2 + 1) / 3 * 2)
        print(cnt + i - (4 - i % 3) % 3 - (mintCnt - n) * 3)


if __name__ == "__main__":
    main()
