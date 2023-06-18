def main():
    n = int(input())
    m = int(input())
    adjectives = [input() for _ in range(n)]
    nouns = [input() for _ in range(m)]
    for adjective in adjectives:
        for noun in nouns:
            print(adjective, "as", noun)


if __name__ == "__main__":
    main()
