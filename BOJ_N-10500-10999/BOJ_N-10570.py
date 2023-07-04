def main():
    N = int(input())
    for _ in range(N):
        V = int(input())
        nums = {}
        for _ in range(V):
            S = int(input())
            try:
                nums[S] += 1
            except KeyError:
                nums[S] = 1
        nums = sorted(nums.items(), key=lambda k: (-k[1], k[0]))
        print(nums[0][0])


if __name__ == "__main__":
    main()
