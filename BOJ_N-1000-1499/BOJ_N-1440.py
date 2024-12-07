def main():
    D1, D2, D3 = map(int, input().split(":"))

    cnt = 0
    if D1 == D2 == D3 == 0:
        cnt += 0
    if 0 < D1 <= 12 and 0 <= D2 <= 59 and 0 <= D3 <= 59:
        cnt += 2
    if 0 < D2 <= 12 and 0 <= D3 <= 59 and 0 <= D1 <= 59:
        cnt += 2
    if 0 < D3 <= 12 and 0 <= D1 <= 59 and 0 <= D2 <= 59:
        cnt += 2

    print(cnt)


if __name__ == "__main__":
    main()
