def main():
    while True:
        h, w = map(int, input().split())

        if h == w == 0:
            break

        square = []
        for hh in range(1, 150):
            for ww in range(hh+1, 151):
                d1 = (h**2 + w**2) ** 0.5
                d2 = (hh**2 + ww**2) ** 0.5
                if d2 > d1:
                    square.append([hh, ww, d2])
                elif d2 == d1 and hh > h:
                    square.append([hh, ww, d2])

        square.sort(key=lambda k: (k[2], k[0]))

        print(*square[0][:2])


if __name__ == "__main__":
    main()
