def main():
    nums = sorted(map(int, input().split()))
    A, B = nums[0], nums[1]
    C = nums[-1] - A - B
    print(A, B, C)


if __name__ == "__main__":
    main()
