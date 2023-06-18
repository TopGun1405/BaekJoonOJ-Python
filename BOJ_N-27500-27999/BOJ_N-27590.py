def main():
    ds, ys = map(int, input().split())
    dm, ym = map(int, input().split())
    s, m = ys - ds, ym - dm
    while s != m:
        if s > m:
            m += ym
        else:
            s += ys
    print(s)


if __name__ == "__main__":
    main()
