def main():
    s = input()

    S = "UAPC"
    for c in s:
        S = S.replace(c, "")

    print(S)


if __name__ == "__main__":
    main()
