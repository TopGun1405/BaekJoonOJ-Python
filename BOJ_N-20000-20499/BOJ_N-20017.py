def main():
    n, m, a = map(int, input().split())
    b = list(map(int, input().split()))

    tot = 0
    for floor in range(n-1):
        for room in range(m):
            i = floor * m + room
            j = i + m
            if b[j] > 2 * b[i]:
                tot += a

    print(tot)


if __name__ == "__main__":
    main()
