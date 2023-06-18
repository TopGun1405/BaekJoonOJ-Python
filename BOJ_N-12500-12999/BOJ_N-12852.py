def main():
    N = int(input())
    mTimes = [0] * (N + 1)
    nums = [[1]] * (N + 1)
    for i in range(2, N + 1):
        mTimes[i] = mTimes[i - 1] + 1
        nums[i] = nums[i - 1] + [i]
        if i % 3 == 0 and mTimes[i // 3] + 1 < mTimes[i]:
            mTimes[i] = mTimes[i // 3] + 1
            nums[i] = nums[i // 3] + [i]
        if i % 2 == 0 and mTimes[i // 2] + 1 < mTimes[i]:
            mTimes[i] = mTimes[i // 2] + 1
            nums[i] = nums[i // 2] + [i]
    print(mTimes[N])
    print(*nums[N][::-1])


if __name__ == "__main__":
    main()
