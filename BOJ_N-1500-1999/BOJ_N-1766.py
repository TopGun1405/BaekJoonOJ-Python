import heapq


def main():
    N, M = map(int, input().split())
    ques = [[0]] + [[] for _ in range(N)]
    indegree = [0] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        ques[A].append(B)
        indegree[B] += 1

    heap = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        currQ = heapq.heappop(heap)
        print(currQ, end=' ')
        for i in ques[currQ]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(heap, i)


if __name__ == "__main__":
    main()
