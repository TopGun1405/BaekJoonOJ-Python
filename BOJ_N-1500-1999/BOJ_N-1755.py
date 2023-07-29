def main():
    M, N = map(int, input().split())

    n = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four",
         '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}
    nums = [[i, ''.join(n[c] for c in str(i))] for i in range(M, N + 1)]
    nums.sort(key=lambda k: k[1])
    for n in range(len(nums)):
        if n % 10 == 0 and n != 0:
            print()
        print(nums[n][0], end=' ')


if __name__ == "__main__":
    main()
