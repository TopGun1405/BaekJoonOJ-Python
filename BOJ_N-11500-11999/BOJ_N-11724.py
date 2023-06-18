from collections import deque


def countConnectedComponent(graph, visited, n):
    queue = deque([n])
    visited[n] = True
    while queue:
        currN = queue.popleft()
        for i in graph[currN]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


def main():
    N, M = map(int, input().split())
    graph = {n: set() for n in range(1, N + 1)}
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)

    visited = [False] * (N + 1)
    ans = 0
    for u in range(1, N + 1):
        if visited[u]:
            continue
        countConnectedComponent(graph, visited, u)
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
