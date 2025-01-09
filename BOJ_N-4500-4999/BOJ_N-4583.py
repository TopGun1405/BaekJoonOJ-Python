def main():
    mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

    while True:
        S = input()[::-1]

        if S == "#":
            break

        rev_S = ""
        for c in S:
            if c in ["i", "o", "v", "w", "x"]:
                rev_S += c
            elif c in mirror:
                rev_S += mirror[c]

        if len(rev_S) == len(S):
            print(rev_S)
        else:
            print("INVALID")


if __name__ == "__main__":
    main()
