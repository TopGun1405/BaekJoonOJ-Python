def main():
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            a, b = query[1:]
            print(sum(nums[a-1:b]))
            nums[a-1], nums[b-1] = nums[b-1], nums[a-1]
        elif query[0] == 2:
            a, b, c, d = query[1:]
            print(sum(nums[a-1:b]) - sum(nums[c-1:d]))


if __name__ == "__main__":
    main()
