def main():
    M, N = map(int, input().split())
    nums = {n: 0 for n in range(10)}
    for n in range(M, N + 1):
        for i in str(n):
            nums[int(i)] += 1
    print(*nums.values())


if __name__ == "__main__":
    main()
