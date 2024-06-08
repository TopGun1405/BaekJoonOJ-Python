def main():

    def lotto(idx):
        if len(num_lotto) == 6:
            print(*num_lotto)
            return
        for i in range(idx, len(S)):
            num_lotto.append(S[i])
            lotto(i + 1)
            num_lotto.pop()

    while True:
        test_case = list(map(int, input().split()))

        if test_case[0] == 0:
            break

        k, S = test_case[0], test_case[1:]
        num_lotto = []

        lotto(0)
        print()


if __name__ == "__main__":
    main()
