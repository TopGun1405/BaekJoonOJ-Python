def main():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())

        dis = y - x
        n = round(dis ** 0.5)
        if abs(n ** 2 - dis) <= n:
            if dis <= n ** 2:
                print(2 * n - 1)
            else:
                print(2 * n)


if __name__ == "__main__":
    main()
