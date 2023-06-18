def main():
    T = int(input())
    for _ in range(T):
        m, n = map(int, input().split())
        box = [input().split() for _ in range(m)]

        res = 0
        for j in range(n):
            cnt = 0
            for i in range(m - 1, -1, -1):
                if box[i][j] == '1':
                    res += cnt
                else:
                    cnt += 1
        print(res)


if __name__ == "__main__":
    main()
