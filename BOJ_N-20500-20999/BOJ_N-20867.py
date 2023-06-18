def main():
    M, S, G = map(int, input().split())
    A, B = map(float, input().split())
    L, R = map(int, input().split())

    fk = 1 / A * L + M / G
    lm = 1 / B * R + M / S
    print("friskus" if fk < lm else "latmask")


if __name__ == "__main__":
    main()
