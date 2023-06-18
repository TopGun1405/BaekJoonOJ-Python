def main():
    N, M = map(int, input().split())
    x = sorted(map(int, input().split()))
    low, high = 0, len(x)
    while low + 1 < high:
        mid = (low + high) // 2
        dis = 0
        for idx, xi in enumerate(x):
            dis = dis + (xi if idx < mid else -xi)
        if dis >= M:
            high = mid
        else:
            low = mid
    print(len(x) - low)


if __name__ == "__main__":
    main()
