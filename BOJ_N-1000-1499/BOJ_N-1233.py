def main():
    S1, S2, S3 = map(int, input().split())

    dice = [0] * 81
    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                dice[i+j+k] += 1

    print(dice.index(max(dice)))


if __name__ == "__main__":
    main()
