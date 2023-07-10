def main():
    n, m = map(int, input().split())
    loc = {i: 0 for i in range(1, m + 1)}
    q = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if q[i][j]:
                loc[j + 1] += 1
    print(*map(lambda e: e[0], sorted(loc.items(), key=lambda k: k[1], reverse=True)))


if __name__ == "__main__":
    main()
