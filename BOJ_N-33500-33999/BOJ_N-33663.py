def main():
    h_lo, h_hi = map(int, input().split())
    s_lo, s_hi = map(int, input().split())
    v_lo, v_hi = map(int, input().split())
    R, G, B = map(int, input().split())

    M, m = max(R, G, B), min(R, G, B)
    V = M
    S = 255 * ((V - m) / V)
    if V == R:
        H = (60 * (G - B)) / (V - m)
    elif V == G:
        H = 120 + ((60 * (B - R)) / (V - m))
    else:
        H = 240 + ((60 * (R - G)) / (V - m))

    if H < 0:
        H += 360

    if h_lo <= H <= h_hi and s_lo <= S <= s_hi and v_lo <= V <= v_hi:
        print("Lumi will like it.")
    else:
        print("Lumi will not like it.")


if __name__ == "__main__":
    main()
