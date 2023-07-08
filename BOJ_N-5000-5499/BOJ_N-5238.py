def main():
    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().split()))
        k, nums = nums[0], nums[1:]
        for i in range(k-3):
            if nums[i] + nums[i+1] != nums[i+2]:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
