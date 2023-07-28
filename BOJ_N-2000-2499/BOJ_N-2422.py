def main():
    N, M = map(int, input().split())

    res = N * (N - 1) * (N - 2) // 6
    nums = [set() for _ in range(N)]
    for _ in range(M):
        n, m = map(int, input().split())
        res -= (N - 2) - len(set.union(nums[n - 1], nums[m - 1]))
        nums[n - 1].add(m)
        nums[m - 1].add(n)
    print(res)


if __name__ == "__main__":
    main()
