from collections import deque


def hideAndSeek(n, k):
    maxL = 2 * k + 1
    visited = [False] * maxL
    queue = deque([n])
    secQueue = deque([0])

    visited[0] = True
    while queue:
        currP = queue.popleft()
        sec = secQueue.popleft()
        if currP == k:
            return sec
        else:
            move = [currP * 2, currP + 1, currP - 1]
            for i in range(3):
                if 0 <= move[i] < maxL and not visited[move[i]]:
                    visited[move[i]] = True
                    queue.append(move[i])
                    secQueue.append(sec + 1)


def main():
    N, K = map(int, input().split())
    print(hideAndSeek(N, K) if N <= K else N - K)


if __name__ == "__main__":
    main()
