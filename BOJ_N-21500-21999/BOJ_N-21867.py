def main():
    N = int(input())
    S = input()

    s = ""
    for c in S:
        if c not in "JAVA":
            s += c

    print(s if s else "nojava")


if __name__ == "__main__":
    main()
