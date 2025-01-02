import sys
sys.setrecursionlimit(10 ** 6)


def main():

    def findRoot(v):
        if v != root[v]:
            root[v] = findRoot(root[v])
        return root[v]

    V, E = map(int, input().split())
    root = list(range(V + 1))
    graph = [list(map(int, input().split())) for _ in range(E)]
    graph.sort(key=lambda k: k[2])

    weight = 0
    for S, E, W in graph:
        s, e = findRoot(S), findRoot(E)
        if s != e:
            if s > e:
                root[s] = e
            else:
                root[e] = s
            weight += W
    print(weight)


if __name__ == "__main__":
    main()
