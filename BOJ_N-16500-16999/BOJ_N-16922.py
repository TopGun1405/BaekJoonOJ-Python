def main():

    def createRomanNum(rec, idx):
        if rec == N:
            res.append(sum(nums))
            return

        for i in range(idx, 4):
            nums.append(roman[i])
            createRomanNum(rec+1, i)
            nums.pop()

    N = int(input())

    roman = [1, 5, 10, 50]
    nums, res = [], []
    createRomanNum(0, 0)

    print(len(set(res)))


if __name__ == "__main__":
    main()
