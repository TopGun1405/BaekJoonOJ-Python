def main():
    while True:
        S = input()

        if S == "END":
            break

        alp = [0] * 26
        for c in S:

            if c == " ":
                continue

            i = ord(c) - 65
            if alp[i] + 1 > 1:
                break
            alp[i] += 1
        else:
            print(S)


if __name__ == "__main__":
    main()
