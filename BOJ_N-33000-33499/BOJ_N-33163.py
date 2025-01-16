def main():
    N = int(input())
    S = list(input())

    JOI = {'J': "O", 'O': "I", 'I': "J"}
    for i in range(N):
        S[i] = JOI[S[i]]

    print("".join(S))


if __name__ == "__main__":
    main()
