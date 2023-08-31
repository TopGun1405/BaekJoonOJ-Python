from heapq import heappush, heappop


def main():
    N = int(input())
    heap = []
    for _ in range(N):
        x = int(input())
        if x > 0:
            heappush(heap, [x, 1])
        elif x < 0:
            heappush(heap, [-x, -1])
        else:
            if heap:
                n, s = heappop(heap)
                print(n if s > 0 else -n)
            else:
                print(0)


if __name__ == "__main__":
    main()
