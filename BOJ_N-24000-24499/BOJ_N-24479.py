def main():

    def dfs(V, E, R):
        visited[R] = True
        for x in E[R]:
            if not visited[x]:
                dfs(V, E, x)

    n, m, r = map(int, input().split())
    
    visited = [False] * n


if __name__ == "__main__":
    main()
