def main():
    P = int(input())
    classNum = {1: 0, 2: 0, 3: 0, 4: 0, 'N': 0}
    for _ in range(P):
        Gp, Cp, Np = map(int, input().split())
        if Gp == 1:
            classNum['N'] += 1
        else:
            classNum[Cp] += 1
    nums = list(classNum.values())
    print(sum(nums[:2]))
    print(nums[2])
    print(nums[3])
    print(nums[4])


if __name__ == "__main__":
    main()
