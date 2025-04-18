def main():
    N = int(input())
    nums = [[0 for _ in range(N)] for _ in range(N)]

    n = 1
    top, bottom, left, right = 0, N-1, 0, N-1
    while top <= bottom and left <= right:

        for i in range(left, right+1):
            nums[top][i] = n
            n += 1
        top += 1

        for i in range(top, bottom+1):
            nums[i][right] = n
            n += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                nums[bottom][i] = n
                n += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                nums[i][left] = n
                n += 1
            left += 1

    for row in nums:
        print(*row)


if __name__ == "__main__":
    main()
