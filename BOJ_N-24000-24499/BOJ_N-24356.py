def main():
    t1, m1, t2, m2 = map(int, input().split())
    if t1 * 60 + m1 > t2 * 60 + m2:
        t2 += 24
    t = (t2 * 60 + m2) - (t1 * 60 + m1)
    print(t, t // 30)


if __name__ == "__main__":
    main()
