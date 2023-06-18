def main():
    i = 1
    while True:
        w1, w2 = input(), input()
        if w1 == w2 == "END":
            break

        wl1, wl2 = {chr(n + 97): 0 for n in range(26)}, {chr(n + 97): 0 for n in range(26)}
        for w in w1:
            wl1[w] += 1
        for w in w2:
            wl2[w] += 1

        print("Case {}: {}".format(i, "same" if wl1 == wl2 else "different"))
        i += 1


if __name__ == "__main__":
    main()
