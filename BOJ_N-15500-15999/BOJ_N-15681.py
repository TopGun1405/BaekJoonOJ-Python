import sys
sys.setrecursionlimit(10**9)


def main() -> None:

    def dfs(v: int) -> int:
        visited[v] = 1
        for i in node[v]:
            if visited[i] == -1:
                visited[v] += dfs(i)

        return visited[v]

    N, R, Q = map(int, input().split())

    visited = [-1] * (N + 1)
    node: list[list[int]] = [[] for _ in range(N+1)]
    for _ in range(N-1):
        U, V = map(int, input().split())
        node[U].append(V)
        node[V].append(U)

    dfs(R)

    for _ in range(Q):
        U = int(input())

        print(visited[U])


if __name__ == "__main__":
    main()
