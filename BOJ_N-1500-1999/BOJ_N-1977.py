def main():
    M, N = int(input()), int(input())
    nums, i = [], 1
    while i ** 2 <= N:
        if M <= i ** 2 <= N:
            nums.append(i ** 2)
        i += 1
    if nums:
        print(sum(nums))
        print(nums[0])
    else:
        print(-1)


if __name__ == "__main__":
    main()
