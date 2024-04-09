from heapq import heappop, heappush


def main():
    INF = int(1e9)

    def dijkstra(start: int) -> list:
        queue = []
        heappush(queue, [start, 0])

        distance = [INF] * (N + 1)
        distance[start] = 0

        while queue:
            currV, currCost = heappop(queue)
            if currCost > distance[currV]:
                continue
            for nextV, nextCost in graph[currV]:
                cost = currCost + nextCost
                if cost < distance[nextV]:
                    distance[nextV] = cost
                    heappush(queue, [nextV, cost])

        return distance

    N = int(input())
    M = int(input())
    graph = {n: [] for n in range(1, N + 1)}
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append([e, c])
    A, B = map(int, input().split())

    dist = dijkstra(A)
    print(dist[B])


if __name__ == "__main__":
    main()
