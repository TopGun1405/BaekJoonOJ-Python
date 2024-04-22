def main():
    n, k = map(int, input().split())

    r = []
    for _ in range(n):
        xi, yi, zi = map(float, input().split())
        r.append((xi**2 + yi**2 + zi**2)**0.5)
    r.sort()

    print(r[k-1])


if __name__ == "__main__":
    main()
