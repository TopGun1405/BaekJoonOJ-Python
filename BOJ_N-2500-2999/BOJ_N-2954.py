def main():
    text = input()
    change = {"apa": 'a', "epe": 'e', "ipi": 'i', "opo": 'o', "upu": 'u'}
    for c in change:
        text = text.replace(c, change[c])
    print(text)


if __name__ == "__main__":
    main()
