def main():
    h1, m1, s1 = map(int, input().split(':'))
    h2, m2, s2 = map(int, input().split(':'))
    if s2 < s1:
        s2 += 60
        m2 -= 1
    if m2 < m1:
        m2 += 60
        h2 -= 1
    if h2 < h1:
        h2 += 24
    print((h2 - h1) * 60 ** 2 + (m2 - m1) * 60 + (s2 - s1))


if __name__ == "__main__":
    main()
