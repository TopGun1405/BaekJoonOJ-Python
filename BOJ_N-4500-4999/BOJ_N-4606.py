def main():
    encoding = {' ': "%20", '!': "%21", '$': "%24", '%': "%25", '(': "%28", ')': "%29", '*': "%2a"}
    while True:
        strings = input()

        if strings == "#":
            break

        strings = list(strings)
        for i in range(len(strings)):
            try:
                strings[i] = encoding[strings[i]]
            except KeyError:
                continue

        print("".join(strings))


if __name__ == "__main__":
    main()
