def main():
    N = int(input())
    text = []
    for _ in range(N):
        S, T = input().split()

        for i in range(len(S)):
            if S[i].lower() == "x":
                text.append(T[i].upper())

    print("".join(text))


if __name__ == "__main__":
    main()
