def main():
    N = int(input())
    S = list(input())

    P, C = [], []
    for i in range(N):
        if S[i] == "P":
            P.append(i)
        elif S[i] == "C":
            C.append(i)

    for i in range(min(len(P), len(C))):
        S[P[i]], S[C[i]] = "C", "P"

    print("".join(S))


if __name__ == "__main__":
    main()
