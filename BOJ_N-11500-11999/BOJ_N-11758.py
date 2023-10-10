def main():
    P1 = list(map(int, input().split()))
    P2 = list(map(int, input().split()))
    P3 = list(map(int, input().split()))

    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3

    # cross product
    ccw = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
    if ccw == 0:
        print(0)
    elif ccw > 0:
        print(1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
