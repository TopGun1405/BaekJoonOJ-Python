def main():
    N = int(input())

    nums = [i+1 for i in range(N)]
    while len(nums) > 1:
        for i in range(0, len(nums), 2):
            nums[i] = 0
        while 0 in nums:
            nums.remove(0)

    print(*nums)


if __name__ == "__main__":
    main()
