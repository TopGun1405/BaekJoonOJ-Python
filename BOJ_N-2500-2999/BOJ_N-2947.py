def main():
    nums = list(map(int, input().split()))
    ans = [1, 2, 3, 4, 5]

    while True:
        for i in range(4):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                print(*nums)
        if nums == ans:
            break


if __name__ == "__main__":
    main()
