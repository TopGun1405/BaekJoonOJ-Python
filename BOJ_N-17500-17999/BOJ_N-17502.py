def main():
    N = int(input())
    S = list(input())

    for i in range(N):
        if S[i].isalpha():
            S[-i-1] = S[i]

    for i in range(N):
        if S[i] == "?":
            S[i] = "a"

    print("".join(S))


if __name__ == "__main__":
    main()
