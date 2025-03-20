def main():
    N = int(input())
    words = [input() for _ in range(N)]

    max_len = max(map(lambda e: len(e), words))
    average = ""
    for i in range(max_len):
        total, n = 0, N
        for j in range(N):
            try:
                total += ord(words[j][i])
            except IndexError:
                n -= 1
        average += chr(total // n)

    print(average)


if __name__ == "__main__":
    main()
