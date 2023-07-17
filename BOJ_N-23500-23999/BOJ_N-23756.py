def main():
    N = int(input())
    A0 = int(input())

    degSum = 0
    for _ in range(N):
        AN = int(input())
        degSum += min(abs(A0 - AN), 360 - A0 + AN, A0 + 360 - AN)
        A0 = AN
    print(degSum)


if __name__ == "__main__":
    main()
