def main():
    n = int(input())
    print((11339 - 105 ** 2) ** 0.5)
    i = 0
    while True:
        temp = n
        nums = []
        trial = i
        for _ in range(4):
            nums.append(int(temp ** 0.5) - trial)
            temp -= nums[-1] ** 2
            trial += 1
            print(nums, temp)
        i += 1
        if temp == 0:
            break


if __name__ == "__main__":
    main()
