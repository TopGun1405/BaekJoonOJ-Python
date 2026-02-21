def main():
    N = int(input())
    S = input()

    minTrans = 100
    for i in range(N-4):
        diff = sum(1 for a, b in zip(S[i:i+5], "eagle") if a != b)
        minTrans = min(minTrans, diff)

    print(minTrans)


if __name__ == "__main__":
    main()
