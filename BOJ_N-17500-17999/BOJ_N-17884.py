def main():
    n = int(input())
    d = list(map(int, input().split()))
    nums = [1] * n
    for i, di in enumerate(d):
        nums[di + 1] += i + 1
    print(*nums)


if __name__ == "__main__":
    main()
