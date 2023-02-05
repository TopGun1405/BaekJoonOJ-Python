def main():
    word = input()
    for i in range(len(word)):
        print(chr(ord(word[i]) - 3 + (26 if ord(word[i]) <= 67 else 0)), end='')


if __name__ == "__main__":
    main()
