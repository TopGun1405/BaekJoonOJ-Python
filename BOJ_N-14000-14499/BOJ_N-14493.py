def main():
    N = int(input())

    res = 0
    for _ in range(N):
        a, b = map(int, input().split())
        k = res % (a + b)
        if k < b:
            res += b - k
        res += 1
    print(res)


if __name__ == "__main__":
    main()
