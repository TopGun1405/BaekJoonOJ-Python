from collections import deque


def main():
    N, M = map(int, input().split())
    students = [[0]] + [[] for _ in range(N)]
    indegree = [0] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        students[A].append(B)
        indegree[B] += 1

    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        currSt = queue.popleft()
        print(currSt, end=' ')
        for i in students[currSt]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)


if __name__ == "__main__":
    main()
