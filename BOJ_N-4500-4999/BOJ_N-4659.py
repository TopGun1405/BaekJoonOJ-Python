def solution1():
    while True:
        pwd = input()
        if pwd == "end":
            break

        vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        vCnt, cCnt, currC = 0, 0, ''

        for i in range(len(pwd)):
            if pwd[i] in vowel:
                vCnt, cCnt = vCnt + 1, 0
                vowel[pwd[i]] += 1
            else:
                vCnt, cCnt = 0, cCnt + 1

            if vCnt == 3 or cCnt == 3:
                print(f"<{pwd}> is not acceptable.")
                break

            if not currC:
                currC = pwd[i]
            else:
                if currC == pwd[i] and currC != 'e' and currC != 'o':
                    print(f"<{pwd}> is not acceptable.")
                    break
                else:
                    currC = pwd[i]
        else:
            if len(list(filter(lambda c: vowel[c] > 0, vowel))) == 0:
                print(f"<{pwd}> is not acceptable.")
            else:
                print(f"<{pwd}> is acceptable.")


def main():
    alp = set(chr(n + 97) for n in range(26))
    vow = {'a', 'e', 'i', 'o', 'u'}
    con = alp - vow
    while True:
        pwd = input()
        if pwd == "end":
            break

        vowel = list(filter(lambda c: c in ['a', 'e', 'i', 'o', 'u'], pwd))
        triple = list(filter(lambda c: c * 3 in pwd, pwd))
        double = list(filter(lambda c: c * 2 in pwd and c * 2 != 'ee' != 'oo', pwd))

        print(vowel, triple, double)


if __name__ == "__main__":
    main()
