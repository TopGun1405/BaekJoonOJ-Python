def main():
    N, M = map(int, input().split())

    nums = {}
    for n in range(1, N+1):
        for m in range(1, M+1):
            try:
                nums[n+m] += 1
            except KeyError:
                nums[n+m] = 1

    nums = sorted(nums.items(), key=lambda k: (-k[1], k[0]))
    print(*list(map(lambda e: e[0], filter(lambda e: e[1] == nums[0][1], nums))), sep="\n")


if __name__ == "__main__":
    main()
