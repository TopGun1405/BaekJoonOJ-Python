def main():
    a, b, n, w = map(int, input().split())

    res = []
    for i in range(1, n):
        if a * i + (n - i) * b == w:
            res.append((i, n - i))

    if len(res) == 1:
        print(*res[0])
    else:
        print(-1)


if __name__ == "__main__":
    main()
