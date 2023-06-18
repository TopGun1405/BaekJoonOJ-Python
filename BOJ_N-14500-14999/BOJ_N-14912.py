def main():
    n, d = map(int, input().split())
    num = [str(i) for i in range(1, n + 1)]
    tot = 0
    for c in num:
        tot += c.count(str(d))
    print(tot)


if __name__ == "__main__":
    main()
