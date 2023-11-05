def main():
    word = input()
    frame = [[] for _ in range(5)]
    for i, c in enumerate(word):
        dhead, dtail = ("." if i == 0 else ""), ("." if i == len(word) - 1 else "")
        shead, stail = ("#" if i == 0 else ""), ("#" if i == len(word) - 1 else "")
        if (i + 1) % 3 == 0:
            frame[0].append("..*..")
            frame[1].append(".*.*.")
            frame[2].append("*." + c + ".*")
            frame[3].append(".*.*.")
            frame[4].append("..*..")
        elif (i + 1) % 3 == 1:
            frame[0].append(dhead + ".#." + dtail)
            frame[1].append(dhead + "#.#" + dtail)
            frame[2].append(shead + "." + c + "." + stail)
            frame[3].append(dhead + "#.#" + dtail)
            frame[4].append(dhead + ".#." + dtail)
        elif (i + 1) % 3 == 2:
            frame[0].append("..#." + dtail)
            frame[1].append(".#.#" + dtail)
            frame[2].append("#." + c + "." + stail)
            frame[3].append(".#.#" + dtail)
            frame[4].append("..#." + dtail)

    for row in frame:
        print(*row, sep='')


if __name__ == "__main__":
    main()
