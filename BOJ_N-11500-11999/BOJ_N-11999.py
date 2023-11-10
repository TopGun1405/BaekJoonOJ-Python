def main():
    X, Y, M = map(int, input().split())
    res = 0
    for x in range(1_001):
        for y in range(1_001):
            z = x * X + y * Y
            if z <= M:
                res = max(res, z)
    print(res)


if __name__ == "__main__":
    main()
