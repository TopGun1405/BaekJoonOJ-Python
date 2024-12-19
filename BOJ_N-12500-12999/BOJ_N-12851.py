from collections import deque


def main():

    def hideAndSeek(n, k):
        minVal, maxVal = 0, int(1e5)
        queue = deque([N])

        time = [-1] * (maxVal + 1)
        time[n] = 0

        cnt = 0
        while queue:
            current = queue.popleft()
            if current == k:
                cnt += 1

            for move in [current * 2, current + 1, current - 1]:
                if minVal <= move <= maxVal and (time[move] == time[current] + 1 or time[move] == -1):
                    queue.append(move)
                    time[move] = time[current] + 1

        return [time[k], cnt]

    N, K = map(int, input().split())
    print(*hideAndSeek(N, K), sep="\n")


if __name__ == "__main__":
    main()
