def main():
    n = int(input())
    a, b = 100, 100
    for _ in range(n):
        c, s = map(int, input().split())
        if c > s:
            b -= c
        elif c < s:
            a -= s
    print(a)
    print(b)


if __name__ == "__main__":
    main()
