def main():
    text = input()
    time, currP = 0, 'A'
    for c in text:
        l, r = ord(currP) - ord(c), ord(c) - ord(currP)
        time += min(l if l >= 0 else l + 26, r if r >= 0 else r + 26)
        currP = c
    print(time)


if __name__ == "__main__":
    main()
