import sys


def main():
    N = list(map(int, sys.stdin.read().split()))[:-1]

    for n in N:
        nums = []
        for i in range(1, n):
            if n % i == 0:
                if i not in nums:
                    nums.append(i)
                if n // i not in nums and n // i != n:
                    nums.append(n // i)

        s = "ABUNDANT" if sum(nums) > n else ("DEFICIENT" if sum(nums) < n else "PERFECT")
        print(f"{n} {s}")


if __name__ == "__main__":
    main()
