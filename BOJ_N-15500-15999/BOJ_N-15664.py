def main():

    def NandM(idx):
        if len(nums) == M:
            print(*nums)
            return

        latest = 0
        for i in range(idx, N):
            if not visited[i] and latest != A[i]:
                visited[i] = True
                nums.append(A[i])
                latest = A[i]
                NandM(i + 1)
                visited[i] = False
                nums.pop()

    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))

    nums = []
    visited = [False] * N
    NandM(0)


if __name__ == "__main__":
    main()
