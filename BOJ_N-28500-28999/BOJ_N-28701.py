def main():
    N = int(input())
    nums = range(1, N + 1)
    print(sum(nums))
    print(sum(nums) ** 2)
    print(sum(map(lambda n: n ** 3, nums)))


if __name__ == "__main__":
    main()
