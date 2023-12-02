import sys
sys.setrecursionlimit(10 ** 5)


def main():
    def dfs(node, weight):
        left, right = 0, 0
        for nextNode, nextWeight in graph[node]:
            w = dfs(nextNode, nextWeight)
            if left <= right:
                left = max(left, w)
            else:
                right = max(right, w)
        dist['MAX'] = max(dist['MAX'], left + right)
        return max(left + weight, right + weight)

    V = int(input())
    graph = [[] for _ in range(V + 1)]
    for _ in range(V):
        info = list(map(int, input().split()))
        s = info[0]
        for e, v in zip(info[1:-1:2], info[2:-1:2]):
            graph[s].append([e, v])

    dist = {'MAX': 0}
    dfs(1, 0)
    print(dist['MAX'])


if __name__ == "__main__":
    main()
