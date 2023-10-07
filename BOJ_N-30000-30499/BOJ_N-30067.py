def main():
    nums = [int(input()) for _ in range(10)]
    for num in nums:
        if sum(nums) == 2 * num:
            print(num)
            break


if __name__ == "__main__":
    main()
