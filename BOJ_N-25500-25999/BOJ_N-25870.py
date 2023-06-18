def main():
    S = input()
    cntS = dict()
    for s in S:
        if s not in cntS:
            cntS.update({s: 1})
        else:
            cntS[s] += 1
    odd = len(list(filter(lambda c: cntS[c] % 2 == 1, cntS)))
    even = len(list(filter(lambda c: cntS[c] % 2 == 0, cntS)))
    print(0 if odd == 0 else (1 if even == 0 else 2))


if __name__ == "__main__":
    main()
