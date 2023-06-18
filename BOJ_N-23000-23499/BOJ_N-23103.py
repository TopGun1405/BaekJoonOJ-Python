def main():
    N = int(input())
    x1, y1 = map(int, input().split())
    d = 0
    for _ in range(N - 1):
        xi, yi = map(int, input().split())
        d += abs(xi - x1) + abs(yi - y1)
        x1, y1 = xi, yi
    print(d)


if __name__ == "__main__":
    main()
