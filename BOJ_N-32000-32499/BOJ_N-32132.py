def main():
    N = int(input())
    S = input()

    while True:
        if "PS4" in S or "PS5" in S:
            S = S.replace("PS4", "PS").replace("PS5", "PS")
        else:
            break

    print(S)


if __name__ == "__main__":
    main()
