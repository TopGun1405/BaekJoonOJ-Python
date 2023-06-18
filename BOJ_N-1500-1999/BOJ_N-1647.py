def main():

    def findRoot(v):
        if v != root[v]:
            root[v] = findRoot(root[v])
        return root[v]

    N, M = map(int, input().split())
    root = list(range(N + 1))
    graph = [list(map(int, input().split())) for _ in range(M)]
    graph.sort(key=lambda k: k[2])

    cost, div = 0, 0
    for S, E, W in graph:
        s, e = findRoot(S), findRoot(E)
        if s != e:
            if s > e:
                root[s] = e
            else:
                root[e] = s
            cost, div = cost + W, max(div, W)
    print(cost - div)


if __name__ == "__main__":
    main()
