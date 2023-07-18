def main():
    nouns = ['a', 'e', 'i', 'o', 'u']
    word = input()
    msg, chk = 1, 1 if word[0] in nouns else 0
    for c in word[1:]:
        chk = chk + (1 if c in nouns else -1)
        if chk > 1 or chk < 0:
            msg = 0
            break
    print(msg)


if __name__ == "__main__":
    main()
