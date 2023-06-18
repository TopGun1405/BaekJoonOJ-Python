def main():
    N = int(input())
    x, y = [], []
    for _ in range(N):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    print((max(x) - min(x) + max(y) - min(y)) * 2)


if __name__ == "__main__":
    main()
