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
    graph = {n: [] for n in range(1, N + 1)}
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    v1, v2 = map(int, input().split())

    res, minDis = dijkstra(1), INF
    for i in range(1, N + 1):
        if v1 in graph[i] and v2 in graph[i]:
            minDis = min(minDis, res[i])
        else:
            continue
    print(minDis)


if __name__ == "__main__":
    main()
