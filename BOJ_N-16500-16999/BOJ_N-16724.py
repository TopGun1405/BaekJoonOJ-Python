def main():

    def find(v):
        if v != node[v]:
            node[v] = find(node[v])
        return node[v]

    # def find(v):
    #     while v != node[v]:
    #         v = node[v]
    #     return v

    def union(a, b):
        s, e = find(a), find(b)
        if s > e:
            node[s] = e
        else:
            node[e] = s

    N, M = map(int, input().split())
    mapinfo: list = [list(input()) for _ in range(N)]
    node = list(range(N * M))
    visited = [False] * (N * M)
    move = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}

    for i in range(N * M):
        r, c = i // M, i % M
        dx, dy = move[mapinfo[r][c]]
        x, y = c + dx, r + dy
        A, B = i, x + y * M
        if find(A) != find(B) and 0 <= B < N * M:
            union(A, B)

    safeZone = 0
    for i in range(N * M):
        if not visited[find(node[i])]:
            safeZone += 1
            visited[node[i]] = True
    print(safeZone)


if __name__ == "__main__":
    main()
