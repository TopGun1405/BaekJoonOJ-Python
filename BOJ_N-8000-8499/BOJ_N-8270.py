def main():
    n = int(input())
    nums = set(map(int, input().split()))
    print(15_000 - len(nums))


if __name__ == "__main__":
    main()
