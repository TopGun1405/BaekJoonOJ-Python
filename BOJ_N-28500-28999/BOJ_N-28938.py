def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print("Stay" if sum(nums) == 0 else ("Left" if sum(nums) < 0 else "Right"))


if __name__ == "__main__":
    main()
