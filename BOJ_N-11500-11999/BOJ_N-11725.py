import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)


def main():

    # out of memory
    def findParentDFS(parent):
        for node in tree[parent]:
            if parents[node] == 0:
                parents[node] = parent
                findParentDFS(node)

    def findParentBFS(start):
        queue = deque([start])
        while queue:
            parent = queue.popleft()
            for node in tree[parent]:
                if parents[node] == 0:
                    parents[node] = parent
                    queue.append(node)

    N = int(input())
    tree = {n: [] for n in range(1, N + 1)}
    # tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        s, e = map(int, input().split())
        tree[s].append(e)
        tree[e].append(s)
    parents = [None, -1] + [0] * (N - 1)

    # findParentDFS(1)
    findParentBFS(1)
    print(*parents[2:], sep='\n')


if __name__ == "__main__":
    main()
