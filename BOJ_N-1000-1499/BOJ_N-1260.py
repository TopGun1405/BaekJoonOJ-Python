from collections import deque


# fix require
def DFS(graph, V, visited):
    for v in graph[V]:
        if v not in visited:
            visited.append(v)
            DFS(graph, v, visited)
    return visited


def BFS(graph, V):
    visited = [V]
    queue = deque(graph[V])
    while queue:
        currV = queue.popleft()
        if currV not in visited:
            visited.append(currV)
            queue += graph[currV]
    return visited


def main():
    N, M, V = map(int, input().split())
    graph = {n: [] for n in range(1, N + 1)}
    for _ in range(M):
        S, E = map(int, input().split())
        if E not in graph[S]:
            graph[S].append(E)
        if S not in graph[E]:
            graph[E].append(S)
    for v in graph:
        graph[v].sort()
    print(*DFS(graph, V, [V]))
    print(*BFS(graph, V))


if __name__ == "__main__":
    main()
