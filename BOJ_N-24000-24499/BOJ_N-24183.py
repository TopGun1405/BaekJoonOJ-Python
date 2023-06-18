def main():
    a, b, c = map(int, input().split())
    e, p, s = 229 * 324 * a * 2, 297 * 420 * b * 2, 210 * 297 * c
    print("{:.6f}".format((e + p + s) * 10 ** (-6)))


if __name__ == "__main__":
    main()
