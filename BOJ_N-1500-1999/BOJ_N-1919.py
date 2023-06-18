def main():
    S1, S2 = list(input()), list(input())
    s1, s2 = S1[:], S2[:]
    change1 = [c for c in S1 if c not in s2 or s2.remove(c)]
    change2 = [c for c in S2 if c not in s1 or s1.remove(c)]
    print(len(change1) + len(change2))


if __name__ == "__main__":
    main()
