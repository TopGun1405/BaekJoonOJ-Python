def main():
    pref_y = [0] * 1_001
    for y in range(1, 1_001):
        if y % 3 == 0:
            pref_y[y] = pref_y[y-1] + 200
        else:
            pref_y[y] = pref_y[y-1] + 195

    normal = [0] * 11
    for m in range(1, 11):
        normal[m] = normal[m-1] + (20 if m % 2 == 1 else 19)

    special = [0] * 11
    for m in range(1, 11):
        special[m] = special[m-1] + 20

    n = int(input())
    for _ in range(n):
        Y, M, D = map(int, input().split())

        d = pref_y[Y-1]
        if Y % 3 == 0:
            d += special[M-1]
        else:
            d += normal[M-1]
        d += D-1

        print(pref_y[999] - d)


if __name__ == "__main__":
    main()
