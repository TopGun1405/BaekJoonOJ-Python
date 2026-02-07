def main():
    n, m, p = map(int, input().split())

    cnt = 0
    for w in range(1, n+1):
        for h in range(1, m+1):
            if 2 * (w + h) >= p:
                cnt += (n+1-w) * (m+1-h)

    print(cnt)


if __name__ == "__main__":
    main()
