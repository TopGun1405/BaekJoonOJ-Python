def main():
    n = int(input())
    S = list(input())

    for i in range(n):
        S[i] = S[i].lower() if S[i].isupper() else S[i].upper()

    print("".join(S))


if __name__ == "__main__":
    main()
