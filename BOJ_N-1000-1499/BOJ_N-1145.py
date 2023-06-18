def main():
    nums = list(map(int, input().split()))
    num = min(nums)
    while True:
        k = 0
        for i in range(5):
            if num % nums[i] == 0:
                k += 1
        if k > 2:
            print(num)
            break
        num += 1


if __name__ == "__main__":
    main()
