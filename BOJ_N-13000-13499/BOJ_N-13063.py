def main():
    while True:
        n, m, k = map(int, input().split())

        if n == m == k == 0:
            break

        majority = n//2 + 1
        curr_sup = m
        needed = majority - curr_sup

        if needed <= 0:
            print(0)
        elif needed <= n - m - k:
            print(needed)
        else:
            print(-1)


if __name__ == "__main__":
    main()
