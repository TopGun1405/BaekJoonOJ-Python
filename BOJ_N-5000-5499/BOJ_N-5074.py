def main():
    while True:
        s, d = input().split()
        sh, sm = map(int, s.split(':'))
        dh, dm = map(int, d.split(':'))
        if sh == sm == dh == dm == 0:
            break
        t = (sh * 60 + sm) + (dh * 60 + dm)
        n = t // 60 // 24
        h = t // 60 % 24
        m = t % 60
        print("{:02}:{:02} +{}".format(h, m, n) if n > 0 else "{:02}:{:02}".format(h, m))


if __name__ == "__main__":
    main()
