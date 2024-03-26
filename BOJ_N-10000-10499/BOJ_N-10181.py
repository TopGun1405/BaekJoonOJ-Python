def main():
    while True:
        n = int(input())

        if n == -1:
            break

        nums = [i for i in range(2, n // 2 + 1) if n % i == 0]
        if sum(nums) == n - 1:
            print(f"{n} = 1 + {' + '.join(map(str, nums))}")
        else:
            print(f"{n} is NOT perfect.")


if __name__ == "__main__":
    main()
