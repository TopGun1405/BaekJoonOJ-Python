def main():
    INF = int(1e9)

    def bellmanFord(start):
        dis[start] = 0
        for i in range(N):
            for j in range(M):
                s, e, t = graph[j]
                if dis[s] != INF and dis[e] > dis[s] + t:
                    dis[e] = dis[s] + t
                    if i == N - 1:
                        return True
        return False

    N, M = map(int, input().split())
    graph = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph.append([A, B, C])

    dis = [INF] * (N + 1)
    if bellmanFord(1):
        print(-1)
    else:
        print(*map(lambda v: v if v != INF else -1, dis[2:]), sep="\n")


if __name__ == "__main__":
    main()
