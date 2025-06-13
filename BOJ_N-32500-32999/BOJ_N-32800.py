def main():
    n = int(input())

    res, curr = 0, 0
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        curr += b_i - a_i
        res = max(res, curr)

    print(res)


if __name__ == "__main__":
    main()
