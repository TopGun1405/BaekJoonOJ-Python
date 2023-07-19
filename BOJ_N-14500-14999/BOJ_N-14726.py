def main():
    T = int(input())
    for _ in range(T):
        nums = list(input())
        for i in range(16):
            if i % 2 == 0:
                nums[i] = int(nums[i]) * 2
                nums[i] = str(sum(map(int, str(nums[i])))) if nums[i] >= 10 else str(nums[i])
        print('T' if sum(map(int, nums)) % 10 == 0 else 'F')


if __name__ == "__main__":
    main()
