def main():
    N = int(input())
    S = input()
    emoji = {'H': 0, 'I': 0, 'A': 0, 'R': 0, 'C': 0}
    for s in S:
        if s in emoji:
            emoji[s] += 1
    print(min(emoji.values()))


if __name__ == "__main__":
    main()
