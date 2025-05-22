def main():
    decoder = {'y': "a", 'a': "e", 'e': "i", 'i': "o", 'o': "u", 'u': "y"}

    n = int(input())
    text = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(len(text[i])):
            try:
                if text[i][j].isupper():
                    text[i][j] = decoder[text[i][j].lower()].upper()
                else:
                    text[i][j] = decoder[text[i][j]]
            except KeyError:
                pass

    for i in range(n):
        print("".join(text[i]))


if __name__ == "__main__":
    main()
