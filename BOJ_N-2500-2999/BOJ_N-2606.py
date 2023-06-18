from collections import deque


def main():
    N = int(input())
    computers = {n: set() for n in range(1, N + 1)}
    cNum = int(input())
    for _ in range(cNum):
        c1, c2 = map(int, input().split())
        computers[c1].add(c2)
        computers[c2].add(c1)
        # if c2 not in computers[c1]:
        #     computers[c1].append(c2)
        # if c1 not in computers[c2]:
        #     computers[c2].append(c1)
    visited = [False for _ in range(N + 1)]
    queue = deque([1])
    virus = 0
    while queue:
        c = queue.popleft()
        if not visited[c]:
            queue += computers[c]
            virus += 1
            visited[c] = True
    print(virus - 1)


if __name__ == "__main__":
    main()
