def main():
    N = int(input())
    cow, cnt = {}, 0
    for _ in range(N):
        num, pos = map(int, input().split())
        try:
            if cow[num] != pos:
                cow[num], cnt = pos, cnt + 1
        except KeyError:
            cow[num] = pos
    print(cnt)


if __name__ == "__main__":
    main()
