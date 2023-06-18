def main():
    N = int(input())
    num = list(map(int, input().split()))
    nums = {n: 0 for n in set(num)}

    for n in num:
        nums[n] += 1

    M = int(input())
    find = list(map(int, input().split()))

    for e in find:
        if e in nums:
            print(nums[e], end=' ')
        else:
            print(0, end=' ')


if __name__ == "__main__":
    main()
