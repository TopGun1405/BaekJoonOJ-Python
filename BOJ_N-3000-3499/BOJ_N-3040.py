def main():
    nums = [int(input()) for _ in range(9)]
    tot = sum(nums)
    for i in range(8):
        for j in range(i + 1, 9):
            if tot - (nums[i] + nums[j]) == 100:
                del nums[i]
                del nums[j - 1]
                break
        else:
            continue
        break
    print(*sorted(nums), sep='\n')


if __name__ == "__main__":
    main()
