def main():

    def findRoot(v):
        if v != root[v]:
            root[v] = findRoot(root[v])
        return root[v]

    n = int(input())
    stars = [list(map(float, input().split())) for _ in range(n)]

    root = list(range(n + 1))
    starCost = []
    for iA, starA in enumerate(stars[:-1]):
        for iB, starB in enumerate(stars[iA+1:]):
            ax, ay = starA[0], starA[1]
            bx, by = starB[0], starB[1]
            starCost.append([iA+1, iA+iB+2, ((bx-ax)**2 + (by-ay)**2)**0.5])
    starCost.sort(key=lambda k: k[2])

    cost = 0
    for S, E, W in starCost:
        s, e = findRoot(S), findRoot(E)
        if s != e:
            if s > e:
                root[s] = e
            else:
                root[e] = s
            cost += W
    print("{:0.2f}".format(cost))


if __name__ == "__main__":
    main()
