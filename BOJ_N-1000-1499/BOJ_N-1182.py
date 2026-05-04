def main():
    # incomplete

    # 이진?

    # def subsequence(rec, idx):
    #     if 0 < rec <= N:
    #         tot = 0
    #         for i in range(N):
    #             if visited[i]:
    #                 tot += A[i]
    #         if tot == S:
    #             res['CNT'] += 1
    #
    #     for i in range(idx, N):
    #         if not visited[i]:
    #             visited[i] = True
    #             subsequence(rec+1, i+1)
    #             visited[i] = False

    def subseq(idx, tot):
        if idx >= N:
            return
        tot += A[idx]
        if tot == S:
            res['CNT'] += 1
        subseq(idx+1, tot)
        subseq(idx+1, tot-A[idx])

    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    res = {'CNT': 0}

    # visited = [False] * N
    # subsequence(0, 0)

    subseq(0, 0)

    print(res['CNT'])


if __name__ == "__main__":
    main()
