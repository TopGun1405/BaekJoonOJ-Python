def main():
    N = int(input())
    for _ in range(N):
        n = int(input())

        nums = [i for i in range(1, n) if n % i == 0]
        k = sum(nums)
        if k < n:
            print(f"{n} is a deficient number.")
        elif k == n:
            print(f"{n} is a perfect number.")
        else:
            print(f"{n} is an abundant number.")
        print()


if __name__ == "__main__":
    main()
