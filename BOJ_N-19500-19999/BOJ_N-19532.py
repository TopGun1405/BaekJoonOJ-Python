def main():
    a, b, c, d, e, f = map(int, input().split())
    # brute force
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
                print(x, y)
                break
        else:
            continue
    ########################################################
    k = a * e - b * d
    print((e * c - b * f) // k, (a * f - d * c) // k)


if __name__ == "__main__":
    main()
