def main():

    def sam(tot):
        if len(nums) == N:
            if tot % 3 == 0:
                res['CNT'] += 1
            return

        for n in range(3):
            if len(nums) == N-1 and n == 0:
                continue
            nums.append(n)
            sam(tot + n)
            nums.pop()

    N = int(input())
    nums = []
    res = {'CNT': 0}

    sam(0)

    print(res['CNT'])


if __name__ == "__main__":
    main()
