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

    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        s, e, v = map(int, input().split())
        graph[s].append([e, v])

    dist = {'MAX': 0}
    dfs(1, 0)
    print(dist['MAX'])


if __name__ == "__main__":
    main()
