def main():
    R, G, B = map(int, input().split())

    Rp, Gp, Bp = R / 255, G / 255, B / 255
    K = 1 - max(Rp, Gp, Bp)

    C = (1 - Rp - K) / (1 - K) if K != 1 else 0
    M = (1 - Gp - K) / (1 - K) if K != 1 else 0
    Y = (1 - Bp - K) / (1 - K) if K != 1 else 0

    print(f"{C:.04f} {M:.04f} {Y:.04f} {K:.04f}")


if __name__ == "__main__":
    main()
