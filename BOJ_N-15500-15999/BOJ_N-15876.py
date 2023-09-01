def main():
    n, k = map(int, input().split())
    nums, m = [], 0
    while len(nums) < 5 * n:
        nums, m = nums + list(bin(m)[2:]), m + 1
    print(*nums[k-1::n][:5])


if __name__ == "__main__":
    main()
