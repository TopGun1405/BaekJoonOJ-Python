def main():
    N, M = map(int, input().split())

    asciiArt = [[] for _ in range(N)]
    for n in range(N):
        RGB = list(map(int, input().split()))
        for i in range(0, 3 * M, 3):
            R, G, B = RGB[i], RGB[i+1], RGB[i+2]

            I = 2126*R + 7152*G + 722*B
            if 0 <= I < 510_000:
                asciiArt[n].append("#")
            elif 510_000 <= I < 1_020_000:
                asciiArt[n].append("o")
            elif 1_020_000 <= I < 1_530_000:
                asciiArt[n].append("+")
            elif 1_530_000 <= I < 2_040_000:
                asciiArt[n].append("-")
            elif 2_040_000 <= I:
                asciiArt[n].append(".")

    for row in asciiArt:
        print("".join(row))


if __name__ == "__main__":
    main()
