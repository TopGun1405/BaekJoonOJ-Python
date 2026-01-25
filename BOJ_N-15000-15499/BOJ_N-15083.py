def main():
    p1, p2, p3 = map(int, input().split())
    c1, c2, c3 = map(int, input().split())

    tot = p1 + p2 + p3
    s1 = tot * c1 / 100

    p, c = [p1, p2, p3], [c2, c3]
    s2 = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            s = p[i] * c[0] / 100 + p[j] * c[1] / 100
            s2 = max(s2, s)

    if s1 > s2:
        print(f"one {s1:.2f}")
    else:
        print(f"two {s2:.2f}")


if __name__ == "__main__":
    main()
