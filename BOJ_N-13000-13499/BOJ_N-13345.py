def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    l1 = (x1-x2)**2 + (y1-y2)**2
    l2 = (x2-x3)**2 + (y2-y3)**2
    l3 = (x3-x1)**2 + (y3-y1)**2

    if l1 == l2:
        # ((x1 + x3)/2, (y1 + y3)/2) = ((x2 + x)/2, (y2 + y)/2)
        print(x3+x1-x2, y3+y1-y2)
    elif l2 == l3:
        # ((x1 + x2)/2, (y1 + y2)/2) = ((x3 + x)/2, (y3 + y)/2)
        print(x1+x2-x3, y1+y2-y3)
    else:
        # ((x2 + x3)/2, (y2 + y3)/2) = ((x1 + x)/2, (y1 + y)/2)
        print(x2+x3-x1, y2+y3-y1)


if __name__ == "__main__":
    main()
