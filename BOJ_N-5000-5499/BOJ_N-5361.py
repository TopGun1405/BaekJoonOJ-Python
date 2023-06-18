def main():
    d = [350.34, 230.90, 190.55, 125.30, 180.90]
    t = int(input())
    for _ in range(t):
        p = list(map(int, input().split()))
        print("${:0.2f}".format(d[0] * p[0] + d[1] * p[1] + d[2] * p[2] + d[3] * p[3] + d[4] * p[4]))


if __name__ == "__main__":
    main()
