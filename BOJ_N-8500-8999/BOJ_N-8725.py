def main():
    n = int(input())

    tot = 0
    for _ in range(n):
        nums = list(map(int, input().split()))

        k = max(nums)
        tot += k if k > 0 else 0

    print(tot)


if __name__ == "__main__":
    main()
