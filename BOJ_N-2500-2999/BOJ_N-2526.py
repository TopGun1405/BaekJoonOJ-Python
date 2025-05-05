def main():
    N, P = map(int, input().split())

    nums, res = [], N
    while True:
        res = (res * N) % P

        if res in nums:
            print(len(nums) - nums.index(res))
            break

        nums.append(res)


if __name__ == "__main__":
    main()
