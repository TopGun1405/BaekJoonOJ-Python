def main():
    N = int(input())

    max_nums = []
    for n in range(1, N+1):
        nums = [N, n]

        i = 1
        while True:
            k = nums[i-1] - nums[i]
            if k < 0:
                break
            nums.append(k)
            i += 1

        if len(max_nums) < len(nums):
            max_nums = nums

    print(len(max_nums))
    print(*max_nums)


if __name__ == "__main__":
    main()
