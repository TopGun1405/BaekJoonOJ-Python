def main():
    n = int(input())
    for _ in range(n):
        sentence = input()
        sentence = sentence + ('.' if sentence[-1] != '.' else '')
        print(sentence)


if __name__ == "__main__":
    main()
