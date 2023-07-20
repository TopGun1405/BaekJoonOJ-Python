from heapq import heappush, heappop


def main():
    N = int(input())
    lectures = sorted([list(map(int, input().split())) for _ in range(N)])

    queueT = []
    heappush(queueT, lectures[0][1])

    for lecture in lectures[1:]:
        Si, Ti = lecture
        if Si < queueT[0]:
            heappush(queueT, Ti)
        else:
            heappop(queueT)
            heappush(queueT, Ti)

    print(len(queueT))


if __name__ == "__main__":
    main()
