def main():
    N = int(input())
    codes = list(map(int, input().split()))
    notes = {0: 2, 1: 1, 2: 0.5, 4: 0.25, 8: 0.125, 16: 0.0625}
    length = 0
    for code in codes:
        length += notes[code]
    print(length)


if __name__ == "__main__":
    main()
