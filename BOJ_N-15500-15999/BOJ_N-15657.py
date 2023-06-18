def main():

    def dfs(s, n, m):
        # #########
        if len(s) == m:
            print(' '.join(map(str, s)))
            return
        for num in nums:
            if s and num < s[-1]:
                continue
            s.append(num)
            dfs(s, n, m)
            s.pop()

    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    t = []
    dfs(t, N, M)


if __name__ == "__main__":
    main()
