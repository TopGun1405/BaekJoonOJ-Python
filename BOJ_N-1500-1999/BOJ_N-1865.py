def main():
    INF = int(1e9)

    def bellmanFord(start):
        dis = [INF] * (N + 1)
        dis[start] = 0
        for i in range(N):
            for v in edge:
                s, e, t = v
                if dis[e] > dis[s] + t:
                    dis[e] = dis[s] + t
                    if i == N - 1:
                        return True
        return False

    TC = int(input())
    for _ in range(TC):
        N, M, W = map(int, input().split())
        edge = []
        for _ in range(M):
            S, E, T = map(int, input().split())
            edge.append([S, E, T])
            edge.append([E, S, T])

        for _ in range(W):
            S, E, T = map(int, input().split())
            edge.append([S, E, -T])

        print("YES" if bellmanFord(1) else "NO")


if __name__ == "__main__":
    main()
