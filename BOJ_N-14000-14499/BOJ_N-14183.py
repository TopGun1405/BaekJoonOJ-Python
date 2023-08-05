def main():
    while True:
        m, n = map(int, input().split())
        if m == n == 0:
            break
        key = list(map(int, input().split()))
        trashBoxes = [list(map(int, input().split())) for _ in range(n)]

        cnt = 0
        for box in trashBoxes:
            for k, b in zip(key, box):
                if b > k:
                    break
            else:
                cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
