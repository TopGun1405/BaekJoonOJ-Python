def main():
    N = int(input())
    S = input()

    blocks = {
        'A': ["***", "*.*", "***", "*.*", "*.*"],
        'B': ["***", "*.*", "***", "*.*", "***"],
        'C': ["***", "*..", "*..", "*..", "***"],
        'D': ["***", "*.*", "*.*", "*.*", "***"],
        'E': ["***", "*..", "***", "*..", "***"]
    }
    seqBlock = []
    for i in range(5):
        seqBlock.append("".join(map(lambda c: blocks[c][i], S)))

    print(*seqBlock, sep="\n")


if __name__ == "__main__":
    main()
