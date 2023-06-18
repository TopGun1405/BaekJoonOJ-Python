def main():
    X, Y = map(list, input().split())
    X, Y = X[::-1], Y[::-1]
    while True:
        if X[0] != '0' and Y[0] != '0':
            break
        elif X[0] == '0':
            del X[0]
        elif Y[0] == '0':
            del Y[0]
    S = list(str(int(''.join(X)) + int(''.join(Y))))[::-1]
    while True:
        if S[0] != '0':
            break
        del S[0]
    print(''.join(S))


if __name__ == "__main__":
    main()
