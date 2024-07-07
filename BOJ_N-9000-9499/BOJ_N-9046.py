def main():
    T = int(input())
    for _ in range(T):
        text = input()

        alp = {}
        for c in text:
            if c == " ":
                continue
            if alp.get(c, 0):
                alp[c] += 1
            else:
                alp[c] = 1
        alp = sorted(alp.items(), key=lambda k: k[1], reverse=True)

        print(alp[0][0] if len(alp) == 1 or alp[0][1] > alp[1][1] else "?")


if __name__ == "__main__":
    main()
