def main():
    p, m = map(int, input().split())
    if p < m:
        print(-1)
    else:
        a = (p + m) // 2
        b = (p - m) // 2
        if a + b == p and a - b == m:
            print(a, b)
        else:
            print(-1)


if __name__ == "__main__":
    main()
