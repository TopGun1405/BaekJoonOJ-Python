def main():
    while True:
        n = int(input())
        if n == -1:
            break
        nums = []
        for num in range(1, int(n ** 0.5) + 1):
            if n % num == 0:
                nums.append(num)
                if n // num != n:
                    nums.append(n // num)
        if sum(nums) == n:
            print("{} = {}".format(n, " + ".join(map(str, sorted(nums)))))
        else:
            print(n, "is NOT perfect.")


if __name__ == "__main__":
    main()
