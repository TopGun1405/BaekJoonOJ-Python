def main():
    while True:
        word = input()
        if word == "#":
            break
        for i, c in enumerate(word):
            if c in ["a", "e", "i", "o", "u"]:
                print(word[i:] + word[:i] + "ay")
                break
        else:
            print(word + "ay")


if __name__ == "__main__":
    main()
