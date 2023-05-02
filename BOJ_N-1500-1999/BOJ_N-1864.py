def main():
    octNum = {'-': 0, '\\': 1, '(': 2, '@': 3,
              '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
    while True:
        nums = input()
        if nums == '#':
            break
        ans = 0
        for i, num in enumerate(nums):
            ans += octNum[num] * 8 ** (len(nums) - i - 1)
        print(ans)


if __name__ == "__main__":
    main()
