def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    width, height = 0, 0
    if x1 < x3:
        if x2 < x4:
            width += x4 - x1
        else:
            width += x2 - x1
    else:
        if x2 < x4:
            width += x4 - x3
        else:
            width += x2 - x3

    if y1 < y3:
        if y2 < y4:
            height += y4 - y1
        else:
            height += y2 - y1
    else:
        if y2 < y4:
            height += y4 - y3
        else:
            height += y2 - y3

    print(width ** 2 if width > height else height ** 2)


if __name__ == "__main__":
    main()
