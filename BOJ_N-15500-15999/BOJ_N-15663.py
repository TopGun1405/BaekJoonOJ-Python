def main():

    def dfs(n, m):
        # #########
        if len(t) == m:
            print(*t)
            return
        seq = 0
        for i in range(N):
            if visited[i] or seq == nums[i]:
                continue
            visited[i] = True
            t.append(nums[i])
            seq = nums[i]
            dfs(n, m)
            visited[i] = False
            t.pop()

    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    visited = [False] * N
    t = []
    dfs(N, M)
    

if __name__ == "__main__":
    main()
