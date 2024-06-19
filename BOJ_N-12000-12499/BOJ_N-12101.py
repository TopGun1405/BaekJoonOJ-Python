def main():

    def num_sum(tot):
        if tot >= n:
            if tot == n:
                seq.append(nums[::])
            return

        for i in range(1, 4):
            nums.append(i)
            num_sum(tot+i)
            nums.pop()

    n, k = map(int, input().split())
    seq, nums = [], []

    num_sum(0)
    seq.sort()

    try:
        print("+".join(map(str, seq[k-1])))
    except IndexError:
        print(-1)


if __name__ == "__main__":
    main()
