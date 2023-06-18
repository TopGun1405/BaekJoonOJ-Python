from heapq import heappush, heappop


def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        Q_min, Q_max = [], []
        operated = [False] * k
        for i in range(k):
            op, n = input().split()
            if op == 'I':
                heappush(Q_min, [int(n), i])
                heappush(Q_max, [-int(n), i])
                operated[i] = True
            elif op == 'D':
                if int(n) == -1:
                    while Q_min and not operated[Q_min[0][1]]:
                        heappop(Q_min)
                    if Q_min:
                        operated[Q_min[0][1]] = False
                        heappop(Q_min)
                elif int(n) == 1:
                    while Q_max and not operated[Q_max[0][1]]:
                        heappop(Q_max)
                    if Q_max:
                        operated[Q_max[0][1]] = False
                        heappop(Q_max)
        while Q_min and not operated[Q_min[0][1]]:
            heappop(Q_min)
        while Q_max and not operated[Q_max[0][1]]:
            heappop(Q_max)
        print(Q_max)
        print(Q_min)
        print(operated)
        print(-Q_max[0][0], Q_min[0][0]) if Q_max and Q_min else print("EMPTY")


if __name__ == "__main__":
    main()
