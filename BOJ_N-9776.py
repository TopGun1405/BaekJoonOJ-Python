from math import pi


def main():
    n = int(input())
    maxV = 0
    for _ in range(n):
        g = input().split()
        v = 0
        if g[0] == 'S':
            r = float(g[1])
            v = (4 / 3) * pi * (r ** 3)
        else:
            r, h = float(g[1]), float(g[2])
            if g[0] == 'C':
                v = (1 / 3) * pi * (r ** 2) * h
            elif g[0] == 'L':
                v = pi * (r ** 2) * h
        if v > maxV:
            maxV = v
    print("%0.3f" % maxV)


if __name__ == "__main__":
    main()
