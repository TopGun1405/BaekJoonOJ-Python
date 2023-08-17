def main():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1 or graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1

    for r in graph:
        print(*r)


if __name__ == "__main__":
    main()
