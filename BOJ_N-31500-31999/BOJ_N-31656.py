def main():
    S = input()

    cp, S2 = "", []
    for c in S:
        if cp != c:
            cp = c
            S2.append(c)

    print("".join(S2))


if __name__ == "__main__":
    main()
