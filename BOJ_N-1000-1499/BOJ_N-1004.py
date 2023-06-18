def main():
    T = int(input())

    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        planet = [list(map(int, input().split())) for _ in range(n)]

        count = 0
        for p in planet:
            check1, check2 = False, False
            if (p[0] - x1) ** 2 + (p[1] - y1) ** 2 < p[2] ** 2:
                check1 = True
            if (p[0] - x2) ** 2 + (p[1] - y2) ** 2 < p[2] ** 2:
                check2 = True
            if (check1 and not check2) or (not check1 and check2):
                count = count + 1
        print(count)


if __name__ == "__main__":
    main()
