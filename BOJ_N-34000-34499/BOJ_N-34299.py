def main():
    h1, m1, s1 = map(int, input().split(":"))
    h2, m2, s2 = map(int, input().split(":"))

    h = 1 if h1 < 12 <= h2 else 0
    m = h2 - h1
    s = (h2 - h1) * 60 + (m2 - m1)

    print(h, m, s)


if __name__ == "__main__":
    main()
