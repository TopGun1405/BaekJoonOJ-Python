def main():
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N)]

    c1, c2, c3, c4 = set(), set(), set(), set()
    xp, xm, yp, ym = 0, 0, 0, 0
    for Xi, Yi in pos:
        if Xi > 0 and Yi > 0:
            c1.add(Yi / Xi)
        elif Xi < 0 and Yi > 0:
            c2.add(Yi / Xi)
        elif Xi < 0 and Yi < 0:
            c3.add(Yi / Xi)
        elif Xi > 0 and Yi < 0:
            c4.add(Yi / Xi)
        elif Xi > 0 and Yi == 0:
            xp = 1
        elif Xi < 0 and Yi == 0:
            xm = 1
        elif Xi == 0 and Yi > 0:
            yp = 1
        elif Xi == 0 and Yi < 0:
            ym = 1
    print(len(c1) + len(c2) + len(c3) + len(c4) + xp + xm + yp + ym)


if __name__ == "__main__":
    main()
