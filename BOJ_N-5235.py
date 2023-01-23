def main():
    T = int(input())
    for _ in range(T):
        even, odd = 0, 0
        nums = list(map(int, input().split()))
        for i in range(1, len(nums)):
            if nums[i] % 2:
                odd += nums[i]
            else:
                even += nums[i]
        print("EVEN" if even > odd else ("ODD" if odd > even else "TIE"))


if __name__ == "__main__":
    main()
