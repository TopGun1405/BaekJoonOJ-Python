def main():

    def dfs(s, n, m):
        if len(s) == m:
            print(' '.join(map(str, s)))
            return
        for i in range(1, n + 1):
            s.append(i)
            dfs(s, n, m)
            s.pop()

    N, M = map(int, input().split())
    t = []
    dfs(t, N, M)


if __name__ == "__main__":
    main()
