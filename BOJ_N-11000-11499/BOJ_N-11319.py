def main():
    S = int(input())
    for _ in range(S):
        sentence = input().replace(' ', '')
        vowels = list(filter(lambda s: s in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'], sentence))
        print(len(sentence) - len(vowels), len(vowels))


if __name__ == "__main__":
    main()
