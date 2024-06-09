def main():

    def createPassword(idx):
        if len(pw) == L:
            vowels = list(filter(lambda c: c in ["a", "e", "i", "o", "u"], pw))
            if len(vowels) >= 1 and len(pw) - len(vowels) >= 2:
                print("".join(pw))
            return

        for i in range(idx, C):
            pw.append(alp[i])
            createPassword(i + 1)
            pw.pop()

    L, C = map(int, input().split())
    alp = sorted(input().split())

    pw = []
    createPassword(0)


if __name__ == "__main__":
    main()
