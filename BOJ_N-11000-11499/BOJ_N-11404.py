def main():
    INF = int(1e9)

    def floydWarshall() -> list:
        dis = [[INF] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(n + 1):
                dis[i][j] = graph[i][j]

        for i in range(1, n + 1):
            for A in range(1, n + 1):
                for B in range(1, n + 1):
                    dis[A][B] = min(dis[A][B], dis[A][i] + dis[i][B])

        return dis

    n = int(input())
    m = int(input())
    graph = [[(INF if i != j else 0) for j in range(n + 1)] for i in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c if graph[a][b] == INF else min(graph[a][b], c)
        # if graph[a][b] == INF:
        #     graph[a][b] = c
        # else:
        #     graph[a][b] = min(c, graph[a][b])

    distance = floydWarshall()
    for v in distance[1:]:
        print(*list(map(lambda e: 0 if e == INF else e, v))[1:])


if __name__ == "__main__":
    main()
