def main():

    def findRoot(v):
        if v != root[v]:
            root[v] = findRoot(root[v])
        return root[v]

    N = int(input())
    root = list(range(N + 1))
    planet = [[n] + list(map(int, input().split())) for n in range(1, N + 1)]

    graph = []
    for i in range(1, 4):
        planet.sort(key=lambda k: k[i])
        for ii in range(N-1):
            graph.append((planet[ii][0], planet[ii+1][0], abs(planet[ii][i] - planet[ii+1][i])))
    graph.sort(key=lambda k: k[2])

    cost = 0
    for S, E, W in graph:
        s, e = findRoot(S), findRoot(E)
        if s != e:
            if s > e:
                root[s] = e
            else:
                root[e] = s
            cost += W
    print(cost)


if __name__ == "__main__":
    main()
