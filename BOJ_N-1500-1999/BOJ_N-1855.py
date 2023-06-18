def main():
    K = int(input())
    S = input()

    PWD = []
    for i in range(0, len(S), K):
        PWD.append(list(S[i:i + K]))

    for i in range(len(PWD)):
        if i % 2:
            PWD[i] = PWD[i][::-1]

    for j in range(K):
        for i in range(len(PWD)):
            print(PWD[i][j], end='')


if __name__ == "__main__":
    main()
