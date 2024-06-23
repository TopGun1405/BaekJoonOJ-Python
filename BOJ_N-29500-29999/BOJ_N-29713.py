def main():
    N = int(input())
    alp = input()

    goldChip = {c: 0 for c in "BRONZESILVER"}
    for c in alp:
        try:
            goldChip[c] += 1
        except KeyError:
            continue

    print(min(map(lambda n: n[1]//2 if n[0] == "R" or n[0] == "E" else n[1], goldChip.items())))


if __name__ == "__main__":
    main()
