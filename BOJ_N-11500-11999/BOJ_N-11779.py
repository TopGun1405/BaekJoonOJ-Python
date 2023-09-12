from heapq import heappop, heappush


def main() -> None:
    INF = int(1e9)

    def dijkstra(start: int) -> tuple:
        queue = []
        heappush(queue, [start, 0])

        distance = [INF] * (n + 1)
        distance[start] = 0

        busPath = [start] * (n + 1)
        while queue:
            currV, currCost = heappop(queue)
            if currCost > distance[currV]:
                continue
            for nextV, nextCost in graph[currV]:
                cost = currCost + nextCost
                if cost < distance[nextV]:
                    distance[nextV], busPath[nextV] = cost, currV
                    heappush(queue, [nextV, cost])

        return busPath, distance

    n = int(input())
    m = int(input())
    graph = {nn: [] for nn in range(1, n + 1)}
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append([e, c])
    A, B = map(int, input().split())

    path, dist = dijkstra(A)
    res, V = [], B
    while V != A:
        res.append(V)
        V = path[V]
    res.append(A)

    print(dist[B])
    print(len(res))
    print(*res[::-1])


if __name__ == "__main__":
    main()
