def main():
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))

    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2

    v1 = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
    v2 = (x2-x1) * (y4-y1) - (x4-x1) * (y2-y1)
    v3 = (x4-x3) * (y1-y3) - (x1-x3) * (y4-y3)
    v4 = (x4-x3) * (y2-y3) - (x2-x3) * (y4-y3)

    print(1 if v1 * v2 < 0 and v3 * v4 < 0 else 0)


if __name__ == "__main__":
    main()
