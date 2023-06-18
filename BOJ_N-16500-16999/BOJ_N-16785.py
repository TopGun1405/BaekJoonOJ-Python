def main():
    A, B, C = map(int, input().split())
    day, cnt = 0, 0
    while cnt < C:
        cnt, day = cnt + A, day + 1
        if day % 7 == 0:
            cnt += B
    print(day)


if __name__ == "__main__":
    main()
