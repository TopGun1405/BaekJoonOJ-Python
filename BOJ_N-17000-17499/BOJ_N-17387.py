def main():
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))

    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2

    check = [
        max(x1, x2) < min(x3, x4),
        min(x1, x2) > max(x3, x4),
        max(y1, y2) < min(y3, y4),
        min(y1, y2) > max(y3, y4)
    ]

    for notCrossed in check:
        if notCrossed:
            print(0)
            break
    else:
        v1 = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
        v2 = (x2-x1) * (y4-y1) - (x4-x1) * (y2-y1)
        v3 = (x4-x3) * (y1-y3) - (x1-x3) * (y4-y3)
        v4 = (x4-x3) * (y2-y3) - (x2-x3) * (y4-y3)

        if v1 == v2 == v3 == v4 == 0:
            print(1)
        elif v1 * v2 <= 0 and v3 * v4 <= 0:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
