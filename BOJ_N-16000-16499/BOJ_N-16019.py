def main():
    city = list(map(int, input().split()))

    pref = [0]
    for i in range(len(city)):
        pref.append(pref[-1] + city[i])

    n = len(pref)
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = abs(pref[j] - pref[i])

    for row in mat:
        print(*row)


if __name__ == "__main__":
    main()
