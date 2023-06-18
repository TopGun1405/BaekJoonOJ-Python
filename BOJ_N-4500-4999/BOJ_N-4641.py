def main():
    while True:
        nums = list(map(int, input().split()))
        if nums[-1] == -1:
            break
        nums = list(filter(lambda e: 2 * e in nums, nums[:-1]))
        print(len(nums))


if __name__ == "__main__":
    main()
