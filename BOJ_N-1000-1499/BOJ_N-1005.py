from collections import deque


def main():

    def acmCraft():
        queue = deque()
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
                times[i] = D[i]

        while queue:
            currB = queue.popleft()
            for b in building[currB]:
                indegree[b] -= 1
                times[b] = max(times[b], times[currB] + D[b])
                if indegree[b] == 0:
                    queue.append(b)

    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        D = [0] + list(map(int, input().split()))
        building = [[] for _ in range(N + 1)]
        times = [0] * (N + 1)
        indegree = [0] * (N + 1)
        for _ in range(K):
            X, Y = map(int, input().split())
            building[X].append(Y)
            indegree[Y] += 1
        W = int(input())
        acmCraft()
        print(times[W])


if __name__ == "__main__":
    main()
