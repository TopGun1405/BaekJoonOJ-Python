def main():
    n = int(input())
    nums = set(int(input()) for _ in range(n))
    allN = set(range(1, max(nums) + 1))
    print("good job") if nums == allN else print(*sorted(allN - nums), sep='\n')


if __name__ == "__main__":
    main()
