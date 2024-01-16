def main():
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    res = nums[-1]
    if nums[2] - nums[1] == nums[1] - nums[0]:
        res += nums[1] - nums[0]
    elif nums[2] // nums[1] == nums[1] // nums[0]:
        res *= nums[1] // nums[0]

    print(res)


if __name__ == "__main__":
    main()
