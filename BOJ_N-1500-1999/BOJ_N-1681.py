def main():
    N, L = map(int, input().split())
    num, cnt = 1, 0
    while True:
        if str(L) not in str(num):
            cnt += 1
        if cnt == N:
            print(num)
            break
        num += 1


if __name__ == "__main__":
    main()
