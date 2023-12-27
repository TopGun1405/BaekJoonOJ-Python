def main():
    x1, x2 = map(int, input().split())
    a, b, c, d, e = map(int, input().split())

    def fx_gx(x):
        return (a//3) * (x**3) + (b-d)//2 * (x**2) + (c-e) * x

    print(fx_gx(x2) - fx_gx(x1))


if __name__ == "__main__":
    main()
