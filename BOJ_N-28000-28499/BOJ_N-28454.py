def main():
    YYYY, MM, DD = map(int, input().split('-'))
    N = int(input())
    cnt = 0
    for _ in range(N):
        yyyy, mm, dd = map(int, input().split('-'))
        if yyyy > YYYY:
            cnt += 1
        elif yyyy == YYYY and mm > MM:
            cnt += 1
        elif yyyy == YYYY and mm == MM and dd >= DD:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
