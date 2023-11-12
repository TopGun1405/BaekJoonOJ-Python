def main():
    word = input()

    words = []
    for i in range(1, len(word)):
        for j in range(i + 1, len(word)):
            left, mid, right = word[:i], word[i:j], word[j:]
            words.append(left[::-1] + mid[::-1] + right[::-1])
    words.sort()

    print(words[0])


if __name__ == "__main__":
    main()
