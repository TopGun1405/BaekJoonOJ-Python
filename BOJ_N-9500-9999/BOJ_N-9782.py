def main():
    i = 0
    while True:
        nums = list(map(int, input().split()))
        if nums[0] == 0:
            break
        m = nums[0] // 2
        i += 1
        print("Case {}: {:0.1f}".format(i, nums[m + 1] if nums[0] % 2 else (nums[m] + nums[m + 1]) / 2))


if __name__ == "__main__":
    main()
