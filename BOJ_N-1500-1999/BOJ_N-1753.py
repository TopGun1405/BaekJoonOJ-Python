from heapq import heappop, heappush


def main() -> None:
    INF = int(1e9)

    def dijkstra(start: int) -> list:
        queue = []
        heappush(queue, [0, start])

        distance = [INF] * (V + 1)
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

    V, E = map(int, input().split())
    K = int(input())
    graph = {n: [] for n in range(1, V + 1)}
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    res = dijkstra(K)
    for i in range(1, V + 1):
        print(res[i] if res[i] != INF else "INF")


if __name__ == "__main__":
    main()
