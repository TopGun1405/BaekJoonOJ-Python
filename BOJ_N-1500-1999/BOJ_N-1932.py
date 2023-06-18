def main():
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][j] += tri[i-1][j]
            elif j == i:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
    print(max(tri[n - 1]))


if __name__ == "__main__":
    main()
