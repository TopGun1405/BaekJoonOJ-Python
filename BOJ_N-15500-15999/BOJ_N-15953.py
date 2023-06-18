def main():
    T = int(input())
    for _ in range(T):
        reward = 0
        a, b = map(int, input().split())
        if a == 1:
            reward += 5_000_000
        elif 1 < a <= 3:
            reward += 3_000_000
        elif 3 < a <= 6:
            reward += 2_000_000
        elif 6 < a <= 10:
            reward += 500_000
        elif 10 < a <= 15:
            reward += 300_000
        elif 15 < a <= 21:
            reward += 100_000

        if b == 1:
            reward += 5_120_000
        elif 1 < b <= 3:
            reward += 2_560_000
        elif 3 < b <= 7:
            reward += 1_280_000
        elif 7 < b <= 15:
            reward += 640_000
        elif 15 < b <= 31:
            reward += 320_000

        print(reward)


if __name__ == "__main__":
    main()
