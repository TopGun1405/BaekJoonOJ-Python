def main():
    A, B = map(int, input().split())
    nums = []
    for n in range(1, B + 1):
        if len(nums) < B:
            nums += [n] * n
    print(sum(nums[A-1:B]))


if __name__ == "__main__":
    main()
