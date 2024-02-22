def main():
    N = int(input())
    hayBales = [int(input()) for _ in range(N)]

    tot = sum(hayBales)
    avg = tot / N

    res = 0
    for height in hayBales:
        if height > avg:
            res += height - avg

    print(res)


if __name__ == "__main__":
    main()
