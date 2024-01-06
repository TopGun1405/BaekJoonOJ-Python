def main():

    def dfs(node, cnt):
        visited[node] = True
        if not visited[ans[node]]:
            cnt = dfs(ans[node], cnt + 1)
        return cnt

    N = int(input())
    ans = [0] + [int(input()) for _ in range(N)]

    nums = [0] * (N + 1)
    maxIdx, maxNum = 0, 0
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        nums[i] = dfs(i, 1)
        if nums[i] > maxNum:
            maxIdx, maxNum = i, nums[i]

    print(maxIdx)


if __name__ == "__main__":
    main()
