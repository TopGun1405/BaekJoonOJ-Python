def main():
    text = []
    while True:
        try:
            S = input()
        except EOFError:
            break
        text.append(S.replace("iiing", "th"))

    print(*text, sep="\n")


if __name__ == "__main__":
    main()
