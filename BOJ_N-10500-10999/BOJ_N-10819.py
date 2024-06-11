def main():

    def maxDiff():
        if len(seq) == N:
            val = 0
            for n in range(N-1):
                val += abs(seq[n] - seq[n+1])
            res['MAX'] = max(val, res['MAX'])
            return

        for i in range(N):
            if not visited[i]:
                visited[i] = True
                seq.append(A[i])

                maxDiff()

                seq.pop()
                visited[i] = False

    N = int(input())
    A = list(map(int, input().split()))

    res = {'MAX': 0}
    visited = [False] * N
    seq = []
    maxDiff()

    print(res['MAX'])


if __name__ == "__main__":
    main()
