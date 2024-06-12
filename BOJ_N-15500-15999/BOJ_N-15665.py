def main():

    def NandM():
        if len(nums) == M:
            print(*nums)
            return

        latest = 0
        for i in range(N):
            if latest != A[i]:
                latest = A[i]
                nums.append(A[i])
                NandM()
                nums.pop()

    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))

    nums = []
    NandM()


if __name__ == "__main__":
    main()
    