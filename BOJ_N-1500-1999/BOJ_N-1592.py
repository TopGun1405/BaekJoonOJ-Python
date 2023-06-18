def main():
    N, M, L = map(int, input().split())
    nums = [0] * N
    ans, i = 0, 0
    while nums[i] < M - 1:
        nums[i], ans = nums[i] + 1, ans + 1
        i = (i + (L if nums[i] % 2 else -L)) % N
    print(ans)


if __name__ == "__main__":
    main()
