def main():
    S = input()

    words = []
    for i in range(1, len(S) - 1):
        for j in range(i + 1, len(S)):
            words.append(S[:i][::-1] + S[i:j][::-1] + S[j:][::-1])
    words.sort()

    print(words[0])


if __name__ == "__main__":
    main()
