def main():
    while True:
        n = int(input())
        if n == 0:
            break
        d = ''.join(input().split())
        cnt = 0
        for i in range(n):
            if d[i:i+4] == "2020":
                cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
