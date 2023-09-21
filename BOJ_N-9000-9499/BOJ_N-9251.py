def main():
    S1 = input()
    S2 = input()

    CS_len = [0] * max(len(S1), len(S2))
    for s1 in S1:
        LCS = 0
        for i, s2 in enumerate(S2):
            if LCS < CS_len[i]:
                LCS = CS_len[i]
            elif s1 == s2:
                CS_len[i] = LCS + 1
    print(max(CS_len))


if __name__ == "__main__":
    main()
