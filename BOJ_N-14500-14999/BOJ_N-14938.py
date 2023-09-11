from heapq import heappop, heappush


def main() -> None:
    INF = int(1e9)

    def dijkstra(start: int) -> list:
        queue = []
        heappush(queue, [start, 0])

        distance = [INF] * (n + 1)
        distance[start] = 0

        while queue:
            currV, currDis = heappop(queue)
            for nextV, nextDis in graph[currV].items():
                if currDis + nextDis < distance[nextV]:
                    nextDis += currDis
                    distance[nextV] = nextDis
                    heappush(queue, [nextV, nextDis])

        return distance

    n, m, r = map(int, input().split())
    # t = [0] + [int(k) for k in input().split()]
    t = [0] + list(map(int, input().split()))
    graph = {i: {} for i in range(1, n + 1)}

    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a][b] = l
        graph[b][a] = l

    maxItems = 0
    for s in graph:
        res = dijkstra(s)
        able = filter(lambda e: e[0] <= m, zip(res, t))
        maxItems = max(maxItems, sum([ti for d, ti in able]))

    print(maxItems)


if __name__ == "__main__":
    main()
