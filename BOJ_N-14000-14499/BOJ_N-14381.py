def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())

        k, nums = 1, set()
        while True:
            if k > 100:
                print("Case #{}: {}".format(t, "INSOMNIA"))
                break
            nums = nums | set(str(k * N))
            if len(nums) == 10:
                print("Case #{}: {}".format(t, k * N))
                break
            k += 1


if __name__ == "__main__":
    main()
