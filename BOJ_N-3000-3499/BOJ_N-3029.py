def main():
    hh, mm, ss = map(int, input().split(':'))
    nh, nm, ns = map(int, input().split(':'))
    t1 = hh * 60 ** 2 + mm * 60 + ss
    t2 = nh * 60 ** 2 + nm * 60 + ns
    t = t2 - t1 if t2 > t1 else t2 - t1 + 24 * 60 ** 2
    print("{:02d}:{:02d}:{:02d}".format(t // (60 ** 2), t // 60 % 60, t % 60))


if __name__ == "__main__":
    main()
