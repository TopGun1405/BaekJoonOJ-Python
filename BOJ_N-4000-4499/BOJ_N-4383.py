def main():
    while True:
        try:
            nums = list(map(int, input().split()))
        except EOFError:
            break
        n, nums = nums[0], nums[1:]
        isJolly = set(map(lambda e: abs(e[1] - e[0]), zip(nums[:-1], nums[1:])))
        jolly = set(range(1, n))
        print("Jolly" if jolly & isJolly == jolly else "Not jolly")


if __name__ == "__main__":
    main()
