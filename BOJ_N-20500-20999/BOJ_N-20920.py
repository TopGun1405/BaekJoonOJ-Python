def main():
    N, M = map(int, input().split())
    wordDict = {}
    for _ in range(N):
        word = input()
        try:
            wordDict[word][2] += 1
        except KeyError:
            wordDict[word] = [word, len(word), 1]
    filterDict = sorted(filter(lambda n: n[1] >= M, wordDict.values()),
                        key=lambda k: (-k[2], -k[1], k[0]))
    for word in filterDict:
        print(word[0])


if __name__ == "__main__":
    main()
