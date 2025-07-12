def main():
    while True:
        try:
            n = input()
        except EOFError:
            break

        k, tmp = 0, 0
        nums = set(list(n))
        while len(nums) < 10:
            tmp += int(n)
            nums = nums.union(set(list(str(tmp))))
            k += 1

        print(k)


if __name__ == "__main__":
    main()
