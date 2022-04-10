def main():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        dis = (x2 - x1) ** 2 + (y2 - y1) ** 2

        # same circle
        if dis == 0 and r1 == r2:
            print(-1)
        # inscription, circumscription
        elif (r2 - r1) ** 2 == dis or (r2 + r1) ** 2 == dis:
            print(1)
        # meet at two points
        elif (r2 - r1) ** 2 < dis < (r2 + r1) ** 2:
            print(2)
        # not meeting
        else:
            print(0)


if __name__ == "__main__":
    main()
