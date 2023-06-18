def main():
    while True:
        D, RH, RV = map(float, input().split())
        if D == RH == RV == 0:
            break
        W = 16 * D / (337 ** 0.5)
        H = 9 * W / 16
        DPI_H, DPI_V = RH / W, RV / H
        print("Horizontal DPI: {:.2f}".format(DPI_H))
        print("Vertical DPI: {:.2f}".format(DPI_V))


if __name__ == "__main__":
    main()
