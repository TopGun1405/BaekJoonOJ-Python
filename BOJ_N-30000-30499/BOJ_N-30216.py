def main():
    n = int(input())
    nums = list(map(int, input().split()))

    prev = nums[0]
    cnt, maxLen = 1, 0
    for num in nums[1:]:
        if num > prev:
            cnt += 1
        else:
            maxLen = max(cnt, maxLen)
            cnt = 1
        prev = num

    print(max(cnt, maxLen))


if __name__ == "__main__":
    main()
