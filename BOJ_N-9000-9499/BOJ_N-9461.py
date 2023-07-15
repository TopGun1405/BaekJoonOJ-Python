def main():
    T = int(input())

    nums = [1, 1, 1, 2, 2]
    for i in range(5, 100):
        nums.append(nums[i - 1] + nums[i - 5])

    for _ in range(T):
        N = int(input())
        print(nums[N - 1])


if __name__ == "__main__":
    main()
    