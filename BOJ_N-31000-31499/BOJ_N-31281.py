def main():
    # a, b, c = map(int, input().split())
    # print((a + b + c) - (max(a, b, c) + min(a, b, c)))
    nums = sorted(map(int, input().split()))
    print(nums[1])


if __name__ == "__main__":
    main()
