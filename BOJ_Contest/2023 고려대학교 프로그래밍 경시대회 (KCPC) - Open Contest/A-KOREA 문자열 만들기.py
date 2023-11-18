def main():
    S = input()
    koStr = "KOREA"
    ko = ' '
    for s in S:
        if s == 'K' and (ko[-1] == ' ' or ko[-1] == 'A'):
            ko += s
        elif s == 'O' and ko[-1] == 'K':
            ko += s
        elif s == 'R' and ko[-1] == 'O':
            ko += s
        elif s == 'E' and ko[-1] == 'R':
            ko += s
        elif s == 'A' and ko[-1] == 'E':
            ko += s
    print(len(ko))


if __name__ == "__main__":
    main()
