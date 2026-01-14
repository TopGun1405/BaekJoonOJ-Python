def main():
    T = int(input())
    for _ in range(T):
        nums = list(map(int, input().split()))
        imported = 0
        prev = nums[0]
        for i in range(1, len(nums)-1):
            if nums[i] > 2 * prev:
                imported += nums[i] - 2*prev
            prev = nums[i]

        print(imported)


if __name__ == "__main__":
    main()
