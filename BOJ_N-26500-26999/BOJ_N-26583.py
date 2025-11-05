def main():
    while True:
        try:
            nums = list(map(int, input().split()))
        except EOFError:
            break

        mult = []
        for i in range(len(nums)):
            if i == 0:
                mult.append(nums[i] * nums[i + 1])
            elif i == len(nums) - 1:
                mult.append(nums[i - 1] * nums[i])
            else:
                mult.append(nums[i - 1] * nums[i] * nums[i + 1])

        print(*mult)


if __name__ == "__main__":
    main()
