def main():
    S1, S2 = input(), input()
    seq = 1
    for s1, s2 in zip(S1, S2):
        seq = seq * (1 if s1 == s2 else 2)
    print(seq)


if __name__ == "__main__":
    main()
