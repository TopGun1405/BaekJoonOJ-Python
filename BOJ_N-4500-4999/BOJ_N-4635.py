def main():
    while True:
        n = int(input())
        if n == -1:
            break
        cp, res = 0, 0
        for _ in range(n):
            s, t = map(int, input().split())
            cp, res = t, res + s * (t - cp)
        print("{} miles".format(res))


if __name__ == "__main__":
    main()
