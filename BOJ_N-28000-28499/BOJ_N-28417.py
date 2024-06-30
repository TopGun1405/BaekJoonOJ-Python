def main():
    N = int(input())

    score = 0
    for _ in range(N):
        nums = list(map(int, input().split()))

        run, trick = sorted(nums[:2], reverse=True), sorted(nums[2:], reverse=True)
        score = max(score, run[0] + sum(trick[:2]))

    print(score)


if __name__ == "__main__":
    main()
