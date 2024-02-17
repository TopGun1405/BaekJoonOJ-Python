def main():
    S = input().split()

    s = [S[0][0]]
    ul = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
    for c in S[1:]:
        if c in ul:
            continue
        s.append(c[0])

    print("".join(map(lambda e: e.upper(), s)))


if __name__ == "__main__":
    main()
