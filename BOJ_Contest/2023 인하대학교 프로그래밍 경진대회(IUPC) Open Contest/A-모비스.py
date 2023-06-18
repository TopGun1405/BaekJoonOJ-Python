def main():
    S = input()
    MOBIS = set()
    for c in ['M', 'O', 'B', 'I', 'S']:
        if c in S:
            MOBIS.add(c)
    print(MOBIS)
    print("YES" if len(MOBIS) == 5 else "NO")


if __name__ == "__main__":
    main()
