def main():
    L, D, X = int(input()), int(input()), int(input())
    nums = [k for k in range(L, D + 1) if sum(map(int, str(k))) == X]
    print(nums[0], nums[-1], sep='\n')


if __name__ == "__main__":
    main()
