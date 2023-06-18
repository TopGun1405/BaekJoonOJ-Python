def main():
    N = int(input())
    dice = list(map(int, input().split()))
    if N == 1:
        print(sum(dice) - max(dice))
    else:
        nums = sorted([min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])])
        k1, k2, k3 = (N-2) ** 2 + (N-1) * (N-2) * 4, (N-2) * 4 + (N-1) * 4, 4
        print(k1 * nums[0] + k2 * sum(nums[:2]) + k3 * sum(nums))


if __name__ == "__main__":
    main()
