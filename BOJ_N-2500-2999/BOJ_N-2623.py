from collections import deque


def main():

    def musicProgram():
        result = []
        queue = deque()

        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            currS = queue.popleft()
            result.append(currS)
            for i in singer[currS]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return result

    N, M = map(int, input().split())

    singer = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(M):
        PD = list(map(int, input().split()))
        for s in range(1, PD[0]):
            before, after = PD[s], PD[s + 1]
            singer[before].append(after)
            indegree[after] += 1

    sequence = musicProgram()
    print(0) if len(sequence) != N else print(*sequence, sep='\n')


if __name__ == "__main__":
    main()
