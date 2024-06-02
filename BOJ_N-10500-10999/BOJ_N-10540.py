def main():
    N = int(input())
    x_min, y_min, x_max, y_max = 100, 100, 0, 0
    for _ in range(N):
        X, Y = map(int, input().split())
        x_min, y_min = min(x_min, X), min(y_min, Y)
        x_max, y_max = max(x_max, X), max(y_max, Y)

    print(max(x_max - x_min, y_max - y_min) ** 2)


if __name__ == "__main__":
    main()
