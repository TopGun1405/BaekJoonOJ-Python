def main():

    def dfs(n, m):
        # #########
        if len(t) == m:
            print(*t)
            return
        seq = 0
        for i in range(N):
            if (t and nums[i] < t[-1]) or seq == nums[i]:
                continue
            t.append(nums[i])
            seq = nums[i]
            dfs(n, m)
            t.pop()

    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    t = []
    dfs(N, M)


if __name__ == "__main__":
    main()
