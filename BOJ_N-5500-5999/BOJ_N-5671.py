def main():
    while True:
        try:
            N, M = map(int, input().split())
        except ValueError:
            break
        count_num = 0
        for i in range(N, M + 1):
            temp = []
            while True:
                if i == 0:
                    count_num += 1
                    break
                if i % 10 in temp:
                    break
                else:
                    temp.append(i % 10)
                    i //= 10
        print(count_num)

    # c = 0
    # a = [0] * 5123
    # for i in range(5123):
    #     if len(str(i)) == len(set(str(i))):
    #         c += 1
    #     a[i] = c
    #
    # for e in sys.stdin.readlines():
    #     n, m = map(int, e.split())
    #     print(a[m] - a[n - 1])


if __name__ == "__main__":
    main()