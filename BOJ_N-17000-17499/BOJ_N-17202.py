def main():
    A = list(map(int, input()))
    B = list(map(int, input()))

    nums = [0] * 16
    for i in range(16):
        nums[i] = B[i // 2] if i % 2 else A[i // 2]

    while len(nums) != 2:
        nums = [(a + b) % 10 for a, b in zip(nums[:-1], nums[1:])]

    print(*nums, sep='')


if __name__ == "__main__":
    main()
