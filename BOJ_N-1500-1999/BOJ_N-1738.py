def main():
    INF = int(1e9)

    def bellmanford(start):
        dis[start] = 0

        for i in range(n):
            for node in road:
                U, V, W = node
                if dis[U] != -INF and dis[V] < dis[U] + W:
                    dis[V] = dis[U] + W
                    route[V] = U
                    if i == n - 1:
                        dis[V] = INF

    n, m = map(int, input().split())
    road, route = [], [0] * (n + 1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        road.append([u, v, w])

    dis = [-INF] * (n + 1)
    bellmanford(1)

    res = [n]
    if dis[n] != INF:
        point = n
        while point != 1:
            point = route[point]
            res.append(point)

        print(*res[::-1])
    else:
        print(-1)


if __name__ == "__main__":
    main()
