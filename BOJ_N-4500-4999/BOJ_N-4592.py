def main():
    while True:
        nums = list(map(int, input().split()))
        N, nums = nums[0], nums[1:]

        if N == 0:
            break

        submit = [nums[0]]
        for num in nums[1:]:
            if submit[-1] != num:
                submit.append(num)
        submit.append('$')

        print(*submit)


if __name__ == "__main__":
    main()
