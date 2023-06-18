def main():
    N = int(input())
    mTimes = [0] * (N + 1)
    for i in range(2, N + 1):
        mTimes[i] = mTimes[i - 1] + 1
        if i % 3 == 0:
            mTimes[i] = min(mTimes[i], mTimes[i // 3] + 1)
        if i % 2 == 0:
            mTimes[i] = min(mTimes[i], mTimes[i // 2] + 1)
    print(mTimes[N])


if __name__ == "__main__":
    main()
