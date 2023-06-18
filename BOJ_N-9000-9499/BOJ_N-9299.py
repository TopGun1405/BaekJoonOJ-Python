def main():
    T = int(input())
    for t in range(T):
        nums = list(map(int, input().split()))
        k = nums.pop(0)
        nums.pop()
        nums = [nums[i] * (k - i) for i in range(len(nums))]
        nums.insert(0, k - 1)
        print("Case {}: {}".format(t + 1, ' '.join(map(str, nums))))


if __name__ == "__main__":
    main()
