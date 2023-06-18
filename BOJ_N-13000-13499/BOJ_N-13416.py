def main():
    T = int(input())
    for _ in range(T):
        t = int(input())
        ans = 0
        for _ in range(t):
            nums = list(map(int, input().split()))
            if max(nums) >= 0:
                ans += max(nums)
        print(ans)


if __name__ == "__main__":
    main()
