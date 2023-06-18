from collections import deque
import heapq


class Heap:
    def __init__(self):
        self.heap = deque()

    def heapifyUp(self, k):
        while k > 0 and self.heap[(k-1) // 2] > self.heap[k]:
            self.heap[(k-1) // 2], self.heap[k] = self.heap[k], self.heap[(k-1) // 2]
            k = (k-1) // 2

    def heapifyDown(self, k, n):
        while 2*k + 1 < n:
            left, right = 2*k + 1, 2*k + 2
            minI = left if left < n and self.heap[left] < self.heap[k] else k
            if right < n and self.heap[right] < self.heap[minI]:
                minI = right
            if minI != k:
                self.heap[k], self.heap[minI] = self.heap[minI], self.heap[k]
                k = minI
            else:
                break

    def append(self, k):
        self.heap.append(k)
        self.heapifyUp(len(self.heap) - 1)

    def popleft(self):
        if not self.heap:
            return 0
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        k = self.heap.pop()
        self.heapifyDown(0, len(self.heap))
        return k


def main():
    N = int(input())
    # 1
    heap = Heap()
    for _ in range(N):
        x = int(input())
        if x:
            heap.append(x)
        else:
            print(heap.popleft())

    # 2
    heap = []
    for _ in range(N):
        x = int(input())
        if x:
            heapq.heappush(heap, x)
        else:
            print(heapq.heappop(heap) if heap else 0)


if __name__ == "__main__":
    main()
