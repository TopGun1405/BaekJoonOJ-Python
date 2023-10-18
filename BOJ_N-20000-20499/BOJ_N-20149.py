def ccw(V1: list, V2: list):
    x1, y1, x2, y2 = V1
    x3, y3, x4, y4 = V2

    if max(x1, x2) < min(x3, x4):
        print(0)
        return
    if min(x1, x2) > max(x3, x4):
        print(0)
        return
    if max(y1, y2) < min(y3, y4):
        print(0)
        return
    if min(y1, y2) > max(y3, y4):
        print(0)
        return

    v1 = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
    v2 = (x2-x1) * (y4-y1) - (x4-x1) * (y2-y1)
    v3 = (x4-x3) * (y1-y3) - (x1-x3) * (y4-y3)
    v4 = (x4-x3) * (y2-y3) - (x2-x3) * (y4-y3)

    if v1 * v2 <= 0 and v3 * v4 <= 0:
        print(1)
        if v1 == v2 == v3 == v4 == 0:
            if max(x1, x2) == min(x3, x4) or min(x1, x2) == max(x3, x4):
                if [x1, y1] in [[x3, y3], [x4, y4]]:
                    print(x1, y1)
                elif [x2, y2] in [[x3, y3], [x4, y4]]:
                    print(x2, y2)
        else:
            d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            pre = (x1 * y2 - y1 * x2)
            post = (x3 * y4 - y3 * x4)
            x = (pre * (x3 - x4) - (x1 - x2) * post) / d
            y = (pre * (y3 - y4) - (y1 - y2) * post) / d
            print(x, y)
    else:
        print(0)


def main():
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))

    ccw(L1, L2)


if __name__ == "__main__":
    main()
