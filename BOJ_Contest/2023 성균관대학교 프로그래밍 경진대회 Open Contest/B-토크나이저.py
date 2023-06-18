def main():
    S = input()
    tokS = ''
    for s in S:
        if s == '<' or s == '>' or s == '&&' or s == '||' or s == '(' or s == ')' or s == ' ':
            tokS += ':' + s + ':'
        else:
            tokS += s
    print(tokS)


if __name__ == "__main__":
    main()
