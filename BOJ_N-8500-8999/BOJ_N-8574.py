def main():
    n, k, x, y = map(int, input().split())

    cnt = 0
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        if (x_i - x)**2 + (y_i - y)**2 > k**2:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
