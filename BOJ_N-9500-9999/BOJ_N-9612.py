def main():
    n = int(input())
    words = [input() for _ in range(n)]

    freq = {word: 0 for word in words}
    for word in words:
        freq[word] += 1
    freq = sorted(freq.items(), key=lambda k: (k[1], k[0]), reverse=True)
    print(*freq[0])


if __name__ == "__main__":
    main()
