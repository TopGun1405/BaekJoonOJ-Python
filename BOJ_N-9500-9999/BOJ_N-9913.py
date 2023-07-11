def main():
    N = int(input())
    nums = {}
    for _ in range(N):
        n = int(input())
        try:
            nums[n] += 1
        except KeyError:
            nums[n] = 1
    print(max(nums.values()))


if __name__ == "__main__":
    main()
