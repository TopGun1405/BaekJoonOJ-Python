def main():
    n = int(input())
    P = [list(map(int, input().split())) for _ in range(n)]
    t = int(input())
    for _ in range(t):
        i, dv = map(int, input().split())

        xi, yi = P[i-1]
        cnt = 0
        for xj, yj in P:
            if xi == xj and yi == yj:
                continue
            if (xj - xi)**2 + (yj - yi)**2 <= dv**2:
                cnt += 1

        print(cnt)


if __name__ == "__main__":
    main()
