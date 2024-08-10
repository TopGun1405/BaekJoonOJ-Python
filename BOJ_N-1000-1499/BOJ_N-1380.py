def main():

    notReturned = []
    while True:
        n = int(input())
        if n == 0:
            break
        names = [input() for _ in range(n)]

        nums = []
        for _ in range(2*n-1):
            num, _ = input().split()
            nums.append(int(num))

        nums.sort()
        for i in range(0, 2*n-1, 2):
            if i == 2*n-2 or nums[i] != nums[i+1]:
                notReturned.append(names[nums[i]-1])
                break

    for i, student in enumerate(notReturned):
        print(i+1, student)


if __name__ == "__main__":
    main()
