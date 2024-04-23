from math import pi


def main():
    r, s, h, m, d = map(int, input().split())
    # (h+k):k = s:r
    # k*s = r(h+k) = rh+rk
    # ks-kr = rh
    # k(s-r) = rh
    # k = rh/(s-r)
    k = r*h/(s-r)
    v1 = ((s**2 * pi * (k+h))-(r**2 * pi * k)) / 3

    # (d+k):(h+k) = ?:s
    # ? = s(d+k)/(h+k)
    r2 = s*(d+k)/(h+k)
    v2 = ((r2**2 * pi * (k+d))-(r**2 * pi * k)) / 3

    # (v1-v2):v2 = m:?
    # m*v2 = ?*(v1-v2)
    # ? = m*v2/(v1-v2)
    print(m*v2/(v1-v2))


if __name__ == "__main__":
    main()
