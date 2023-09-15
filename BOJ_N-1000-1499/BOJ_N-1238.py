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

    N, M, X = map(int, input().split())
    graph = {n: [] for n in range(1, N + 1)}
    for _ in range(M):
        S, E, Ti = map(int, input().split())
        graph[S].append([E, Ti])

    res = 0
    for s in graph:
        if s == X:
            continue
        res = max(res, dijkstra(s)[X] + dijkstra(X)[s])
    print(res)


if __name__ == "__main__":
    main()
