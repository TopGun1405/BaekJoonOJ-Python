def main():
    T = int(input())
    for _ in range(T):
        S = input()

        N = len(S)
        if N == 7 and S[0] == S[1] == S[4] and S[2] == S[3] == S[5] == S[6] and S[0] != S[6]:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
