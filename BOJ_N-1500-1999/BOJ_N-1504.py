from heapq import heappop, heappush


def main() -> None:
    INF = int(1e9)

    def dijkstra(start: int) -> list:
        queue = []
        heappush(queue, [0, start])

        distance = [INF] * (N + 1)
        distance[start] = 0

        while queue:
            currDis, currV = heappop(queue)
            if currDis > distance[currV]:
                continue
            for nextV, nextDis in graph[currV]:
                dis = currDis + nextDis
                if dis < distance[nextV]:
                    distance[nextV] = dis
                    heappush(queue, [dis, nextV])

        return distance

    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    v1, v2 = map(int, input().split())

    res = [dijkstra(1), dijkstra(v1), dijkstra(v2)]
    d1 = res[0][v1] + res[1][v2] + res[2][N]
    d2 = res[0][v2] + res[2][v1] + res[1][N]
    print(min(d1, d2) if min(d1, d2) < INF else -1)


if __name__ == "__main__":
    main()
