def main():
    n = int(input())
    for _ in range(n):
        d, f, p = map(float, input().split())
        print("${:0.2f}".format(d * f * p))


if __name__ == "__main__":
    main()
