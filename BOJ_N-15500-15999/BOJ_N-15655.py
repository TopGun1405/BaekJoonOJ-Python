def main():

    def backtracking(n):
        if len(seq) == M:
            print(" ".join(map(str, seq)))
            return
        for i in range(n, N):
            seq.append(nums[i])
            backtracking(i + 1)
            seq.pop()

    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    seq = []
    backtracking(0)


if __name__ == "__main__":
    main()
