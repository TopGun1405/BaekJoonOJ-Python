def main():
    A, B, C = int(input()), int(input()), int(input())
    nums = {str(n): 0 for n in range(10)}
    for n in str(A * B * C):
        nums[n] += 1
    print(*nums.values(), sep='\n')


if __name__ == "__main__":
    main()
