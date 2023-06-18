def main():
    S = input()
    for s in S:
        if s != ' ' and not s.isdigit():
            k = (65 if s.isupper() else 97)
            print(chr((ord(s) + 13 - k) % 26 + k), end='')
        else:
            print(s, end='')


if __name__ == "__main__":
    main()
