def main():
    k, s = map(int, input().split())
    S = input()

    Cryp = []
    for C in S:
        if C == " " or C == "." or C == ",":
            Cryp.append(C)
            continue
        u = 65 if C.isupper() else 97
        i = (ord(C) - u + k) % 26
        Cryp.append(chr(i + u))

    print("".join(Cryp))


if __name__ == "__main__":
    main()
