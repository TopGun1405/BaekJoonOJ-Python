def main():
    N = int(input())

    floor = 1
    for _ in range(N):
        A, B = map(int, input().split())

        d = B - A
        if A < 0 and B > 0:
            floor += d - 1
        elif A > 0 and B < 0:
            floor += d + 1
        else:
            floor += d

    print(floor if floor > 0 else floor - 1)


if __name__ == "__main__":
    main()
