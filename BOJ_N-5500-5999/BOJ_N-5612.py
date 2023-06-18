def main():
    n = int(input())
    m = int(input())
    z, car = 0, m
    for _ in range(n):
        i, o = map(int, input().split())
        m = m + i - o
        if m > car:
            car = m
        if m < 0:
            z = 1
    print(0 if z else car)


if __name__ == "__main__":
    main()
