def main():
    d1, d2, d3 = map(int, input().split())
    a = (d1 + d2 - d3) / 2
    b = (d1 - d2 + d3) / 2
    c = (-d1 + d2 + d3) / 2
    print(-1 if a <= 0 or b <= 0 or c <= 0 else "1\n{} {} {}".format(a, b, c))


if __name__ == "__main__":
    main()
