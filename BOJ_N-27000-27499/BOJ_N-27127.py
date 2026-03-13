def main():
    quotients = []
    for FGHIJ in range(100_000):
        ABCDE = FGHIJ * 9
        if ABCDE < 10_000 or ABCDE > 99_999:
            continue

        s_ABCDE, s_FGHIJ = f"{ABCDE:05d}", f"{FGHIJ:05d}"
        if len(set(s_ABCDE + s_FGHIJ)) == 10:
            quotients.append([s_ABCDE, s_FGHIJ])
    quotients.sort(key=lambda k: int(k[0]))

    N = int(input())

    print(*quotients[N-1])


if __name__ == "__main__":
    main()
