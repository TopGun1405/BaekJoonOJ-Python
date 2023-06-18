def main():
    word = input()
    check = True
    for i in ['U', 'C', 'P', 'C']:
        if i in word:
            word = word[word.index(i) + 1:]
        else:
            check = False
            break
    print("I love UCPC" if check else "I hate UCPC")


if __name__ == "__main__":
    main()
