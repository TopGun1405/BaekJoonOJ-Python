def main():
    N, M = map(int, input().split())
    nums = [n + 1 for n in range(N)]
    for _ in range(M):
        i, j = map(int, input().split())
        nums[i-1:j] = nums[i-1:j][::-1]
    print(*nums)


if __name__ == "__main__":
    main()
