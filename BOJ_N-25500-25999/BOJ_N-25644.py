def main():
    N = int(input())
    aN = list(map(int, input().split()))

    benefit, maxBenefit = 0, 0
    for ai in aN[::-1]:
        benefit = max(benefit, ai)
        maxBenefit = max(maxBenefit, benefit - ai)
    print(maxBenefit)


if __name__ == "__main__":
    main()
