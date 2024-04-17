import sys
sys.setrecursionlimit(10 ** 3)


def main():
    def dfs(node, weight):
        if weight > dist['MAX_VAL']:
            dist['MAX_VAL'] = weight
            dist['MAX_NODE'] = node

        for nextNode, nextWeight in graph[node]:
            if visited[nextNode]:
                continue
            visited[nextNode] = True
            dfs(nextNode, weight + nextWeight)

    V = int(input())
    graph = [[] for _ in range(V + 1)]
    for _ in range(V):
        info = list(map(int, input().split()))
        s = info[0]
        for e, v in zip(info[1:-1:2], info[2:-1:2]):
            graph[s].append([e, v])

    # print(graph)
    dist = {'MAX_VAL': 0, 'MAX_NODE': 0}

    visited = [False] * (V + 1)
    visited[1] = True
    dfs(1, 0)

    visited = [False] * (V + 1)
    visited[dist['MAX_NODE']] = True
    dfs(dist['MAX_NODE'], 0)

    print(dist['MAX_VAL'])


if __name__ == "__main__":
    main()
